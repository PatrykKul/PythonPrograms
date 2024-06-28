from random import randint
from datetime import date
import csv
import os

def log_operation(func):
    def wrapper(*args, **kwargs):
        operation_name = func.__name__
        print(f"Wykonano operację: {operation_name}")
        result = func(*args, **kwargs)
        print(f"Zakończono operację: {operation_name}")
        return result
    return wrapper
def validate_name(name):
    for char in name:
        if not char.isalpha() and char != ' ':
            return False
    return True

def validate_email(email):
    return '@' in email and '.' in email


@log_operation

def add_client():
    id = randint(1000,9999)
    while True:
        name = input("Wprowadz imie i nazwisko: ")
        if validate_name(name):
            break
        else:
            print("Ulica może zawierać tylko litery.")
    while True:
        email = input("Wprowadz e-mail:")
        if validate_email(email):
            break
        else:
            print("Wprowadzono błędny email")

    while True:
        phone = input("Wprowadz nr telefonu:")
        if len(phone) == 9 and phone.isdigit():
            break
        else:
            print("BŁĘDNY NUMER TELEFONU")
    created = date.today()
    updated = date.today()
    print("ADRES: ")
    while True:
        street = input("Wprowadz ulice: ")
        if validate_name(street):
            break
        else:
            print("Ulica może zawierać tylko litery.")
    while True:
        city = input("Wprowadz miasto: ")
        if validate_name(city):
            break
        else:
            print("Miasto może zawierać tylko litery.")
    while True:
        country = input("Wprowadz kraj: ")
        if validate_name(country):
            break
        else:
            print("Kraj może zawierać tylko litery.")
    try:
        with open("customer.csv", mode="a", newline='') as file:
            write = csv.writer(file)
            write.writerow([id,name,email,phone,created,updated])
        with open("address.csv", mode="a", newline='') as file:
            write = csv.writer(file)
            write.writerow([id,street,city,country])
            print("Rejestracja zakonczona pomyslnie.")
    except PermissionError:
        print("Odmowa dostepu do pliku.")
@log_operation
def delete_client_by_id(id):
    try:
        with open("customer.csv", mode="r", newline='') as file:
            reader = csv.reader(file)
            clients = list(reader)
            found = False
        for client in clients:
            if client[0] == id:
                clients.remove(client)
                found = True
                break
        if found:
            with open("customer.csv", mode="w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(clients)
            print("Uzytkownik zostal wyrejestrowany.")
        else:
            print("Nie znaleziono uzytkownika o podanym ID.")

        with open("address.csv", mode="r", newline='') as file:
            reader = csv.reader(file)
            adresy = list(reader)
            found = False
            for adres in adresy:
                if adres[0] == id:
                    adresy.remove(adres)
                    found = True
                    break
        if found:
            with open("address.csv", mode="w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(adresy)
            print("Uzytkownika adres zostal wyrejestrowany.")
        else:
            print("Nie znaleziono adresu uzytkownika o podanym ID.")

    except PermissionError:
        print("Odmowa dostepu do pliku.")
@log_operation
def delete_client_by_name(name):
    try:
        with open("customer.csv", mode="r", newline='') as file:
            reader = csv.reader(file)
            clients = list(reader)
            found = False
            client_id = -5
        for client in clients:
            if client[1] == name:
                client_id = client[0]
                clients.remove(client)
                found = True
                break
        if found:
            with open("customer.csv", mode="w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(clients)
            print("Uzytkownik zostal wyrejestrowany.")
        else:
            print("Nie znaleziono uzytkownika o podanej nazwie.")

        with open("address.csv", mode="r", newline='') as file:
            reader = csv.reader(file)
            adresy = list(reader)
            found = False
            for adres in adresy:
                if adres[0] == client_id:
                    adresy.remove(adres)
                    found = True
                    break
        if found:
            with open("address.csv", mode="w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(adresy)
            print("Uzytkownika adres zostal wyrejestrowany.")
        else:
            print("Nie znaleziono adresu uzytkownika o podanym ID.")

    except PermissionError:
        print("Odmowa dostepu do pliku.")
@log_operation
def borrow_book(client_id, book_id):
    folder_path = "DATABASE"
    file_name = f"{client_id}.csv"
    file_path = os.path.join(folder_path, file_name)
    borrow_date = date.today()

    book_found = False
    book_title = None
    try:
        with open("book.csv", mode="r", newline='') as book_file:
            reader = csv.reader(book_file)
            for row in reader:
                if row[0] == book_id:
                    book_found = True
                    book_title = row[2]
                    break
    except PermissionError:
        print("Odmowa dostępu do pliku 'book.csv'.")

    if book_found:
        if os.path.exists(file_path):
            with open(file_path, "a") as client_file:
                client_file.write(f"{book_id},{book_title},Wypożyczono,{borrow_date},-\n")
            print(f"Książka '{book_title}' została wypożyczona przez klienta o ID {client_id}.")
        else:
            with open(file_path, "w") as client_file:
                client_file.write("Book ID,Title,Status,Borrow Date,Return Date\n")
                client_file.write(f"{book_id},{book_title},Wypożyczono,{borrow_date},-\n")
            print(f"Plik dla klienta o ID {client_id} został utworzony, a książka '{book_title}' została wypożyczona.")
    else:
        print(f"Książka o ID {book_id} nie istnieje w bazie danych.")
@log_operation
def return_book(client_id, book_id, multiple=False):
    def return_multiple_books(client_file, book_id_list):
        return_date = date.today()
        for line in lines:
            parts = line.strip().split(",")
            if parts[0] in book_id_list:
                client_file.write(f"{parts[0]},{parts[1]},Zwrocono,{parts[3]},{return_date}\n")
                print(f"Książki o ID {', '.join(book_id_list)} zostały zwrócone przez klienta o ID {client_id}.")
            else:
                client_file.write(line)

    folder_path = "DATABASE"
    file_name = f"{client_id}.csv"
    file_path = os.path.join(folder_path, file_name)
    return_date = date.today()

    if os.path.exists(file_path):
        with open(file_path, "r") as client_file:
            lines = client_file.readlines()
        with open(file_path, "w") as client_file:
            if multiple:
                return_multiple_books(client_file, book_id)
            else:
                for line in lines:
                    parts = line.strip().split(",")
                    if parts[0] == book_id:
                        client_file.write(f"{parts[0]},{parts[1]},Zwrocono,{parts[3]},{return_date}\n")
                        print(f"Książka o ID {book_id} została zwrócona przez klienta o ID {client_id}.")
                    else:
                        client_file.write(line)
    else:
        print("Plik dla tego klienta nie istnieje. Spróbuj ponownie.")
