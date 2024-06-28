import Obsluga_Ksiazek
import Obsluga_Klienta
import advancedfun
def main():
    print("Witaj w bibliotece!")
    while True:
        print("\nCo chcesz zrobić?")
        print("1. Dodaj/usuń książkę")
        print("2. Dodaj/usuń użytkownika")
        print("3. Wypożycz/Zwróć książkę")
        print("4. Wyjdź z programu")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            choice2 = input("Wpisz 1 by dodać lub 2 by usunąc ksiazke:")
            if choice2 == "1":
                Obsluga_Ksiazek.add_book()
                continue
            elif choice2 == "2":
                choice3 = input("Wybierz po czym usunąć książkę id lub title: ")
                if choice3 == "title":
                    title= input("Podaj tytuł do usuniecia: ")
                    advancedfun.delete_books(advancedfun.delete_by_title, title=title)
                    continue
                elif choice3 == "id":
                    id= input("Podaj id do usuniecia: ")
                    advancedfun.delete_books(advancedfun.delete_by_id, id=id)
                    continue
        if choice == "2":
            choice2 = input("Wpisz 1 by dodać lub 2 by usunąc uzytkownika:")
            if choice2 == "1":
                Obsluga_Klienta.add_client()
                continue

            elif choice2 =="2":
                choice3 = input("Wybierz po czym usunąć uzytkownika id lub name: ")
                if choice3 == "id":
                    id= input("Podaj id uzytkownika do usuniecia: ")
                    advancedfun.delete_clients(advancedfun.delete_client_by_id, id=id)
                elif choice3 =="name":
                    name= input("Podaj nazwe uzytkownika do usuniecia: ")
                    advancedfun.delete_clients(advancedfun.delete_client_by_name, name=name)

        if choice == "3":
            choice2 = input("Wpisz 1 by wypożyczyć lub 2 by zwrócić książkę:")
            if choice2 == "1":
                client_id = input("Podaj id klienta: ")
                book_id = input("Podaj id książki: ")

                Obsluga_Klienta.borrow_book(client_id,book_id)
            elif choice2 == "2":
                choice3 = input("Ile książek chcesz zwrócić? Wpisz 1 lub wiecej: ")
                if choice3 == "1":
                    client_id = input("Podaj id klienta: ")
                    book_id = input("Podaj id książki: ")
                    Obsluga_Klienta.return_book(client_id,book_id)
                elif choice3 =="wiecej":
                    book_list = list()
                    client_id = input("Podaj id klienta: ")
                    print("Wpisz STOP by przestać zwracać książki ")
                    book_id = input("Podaj id książki: ")
                    book_list.append(book_id)
                    while (book_id != "STOP"):
                        book_id = input("Podaj id książki: ")
                        book_list.append(book_id)

                    Obsluga_Klienta.return_book(client_id,book_list,multiple=True)
        elif choice == "4":
            print("Dziękujemy za skorzystanie z biblioteki!")
            break
        else:
            print("Niepoprawny wybór.")

if __name__ == "__main__":
    main()
