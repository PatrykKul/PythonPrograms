
import csv
from datetime import date

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

@log_operation

def add_book():
    try:
        Id = input("wprowadz Id: ")
        while True:
            Author = input("wprowadz authora: ")
            if validate_name(Author):
                break
            else:
                print("Author może zawierać tylko litery")
        Title = input("wprowadz tytul: ")
        while True:
            Pages = input("wprowadz liczbe stron: ")
            if Pages.isdigit():
                break
            else:
                print("Strony muszą być liczbą")

        Created = input("wprowadz date utworzenia: ")
        if(Created == "dzis"):
            Created = date.today()
        Updated = input("wprowadz date aktualizacji: ")
        if(Updated == "dzis"):
            Updated = date.today()
        with open('book.csv', mode='a',newline='') as file:
            write = csv.writer(file)
            write.writerow([Id,Author,Title,Pages,Created,Updated])
            print("Pomyslnie dodano ksiazke")
    except PermissionError:
        print("Odmowa dostepu do plilu.")


@log_operation
def delete_by_id(id):
    try:
        with open("book.csv", mode="r", newline='') as file:
            reader = csv.reader(file)
            books = list(reader)
        found = False
        for book in books:
            if book[0] == id:
                books.remove(book)
                found = True
                break
        if found:
            with open("book.csv", mode="w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(books)
            print("Ksiazka została usunieta pomyslnie.")
        else:
            print("Nie znaleziono książki o podanym ID.")
    except PermissionError:
        print("Odmowa dostepu do pliku.")
@log_operation
def delete_by_title(title):
    try:
        with open("book.csv", mode="r", newline='') as file:
            reader = csv.reader(file)
            books = list(reader)
        found = False
        updated_books = list()
        for book in books:
            if book[2].lower() != title.lower():
                updated_books.append(book)
            else:
                found = True
        if found:
            with open("book.csv", mode="w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(updated_books)
            print("Książka została usunięta pomyślnie.")
        else:
            print("Nie znaleziono książki o podanym tytule.")
    except PermissionError:
        print("Odmowa dostepu do pliku.")
