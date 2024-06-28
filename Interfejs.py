import tkinter as tk
from tkinter import ttk
import Obsluga_Klienta
import Obsluga_Ksiazek

def borrow_or_return(action):
    client_id_value = client_id.get()
    book_id_value = book_id.get()
    if action == "borrow":
        Obsluga_Klienta.borrow_book(client_id_value, book_id_value)
    elif action == "return":
        Obsluga_Klienta.return_book(client_id_value, book_id_value)

def delete_by_id_or_title(action):
    book_title_value = book_title.get()
    book_id_value = book_ids.get()
    if action == "id":
        Obsluga_Ksiazek.delete_by_id(book_id_value)
    elif action == "title":
        Obsluga_Ksiazek.delete_by_title(book_title_value)

def delete_by_id_or_name(action):
    user_name_value = name.get()
    user_id_value = user_id.get()
    if action == "id":
        Obsluga_Klienta.delete_client_by_id(user_id_value)
    elif action == "name":
        Obsluga_Klienta.delete_client_by_name(user_name_value)

def add_user():
    Obsluga_Klienta.add_client()

def add_book():
    Obsluga_Ksiazek.add_book()

root = tk.Tk()
root.title("System Biblioteki")

#styl ramki
style = ttk.Style()
style.configure("TLabelframe", background="lightgray")

# Wypożyczalnia
rentals_frame = ttk.LabelFrame(root, text="Wypożyczalnia", padding=10, style="TLabelframe")
rentals_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

client_id = tk.Entry(rentals_frame, fg='black', font=("Helvetica", 10))
client_id.grid(row=1, column=1, sticky="ew")
client_id.configure(background="white")

book_id = tk.Entry(rentals_frame, fg='black', font=("Helvetica", 10))
book_id.grid(row=2, column=1, sticky="ew")
book_id.configure(background="white")

borrow_button = ttk.Button(rentals_frame, text="Wypożycz", command=lambda: borrow_or_return("borrow"))
borrow_button.grid(row=0, column=0, padx=5, pady=5)
return_button = ttk.Button(rentals_frame, text="Zwróć", command=lambda: borrow_or_return("return"))
return_button.grid(row=0, column=1, padx=5, pady=5)

tk.Label(rentals_frame, text="ID klienta: ").grid(row=1, column=0, sticky="e")
tk.Label(rentals_frame, text="ID książki: ").grid(row=2, column=0, sticky="e")

# Książki
book_frame = ttk.LabelFrame(root, text="Książki", padding=10, style="TLabelframe")
book_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

book_ids = tk.Entry(book_frame, fg='black', font=("Helvetica", 10))
book_ids.grid(row=1, column=1, sticky="ew")
book_ids.configure(background="white")

book_title = tk.Entry(book_frame, fg='black', font=("Helvetica", 10))
book_title.grid(row=2, column=1, sticky="ew")
book_title.configure(background="white")

delete_book_id = ttk.Button(book_frame, text="Usuń po id", command=lambda: delete_by_id_or_title("id"))
delete_book_id.grid(row=0, column=0, padx=5, pady=5)
delete_book_title = ttk.Button(book_frame, text="Usuń po tytule", command=lambda: delete_by_id_or_title("title"))
delete_book_title.grid(row=0, column=1, padx=5, pady=5)

tk.Label(book_frame, text="ID książki: ").grid(row=1, column=0, sticky="e")
tk.Label(book_frame, text="Tytuł książki: ").grid(row=2, column=0, sticky="e")

# Użytkownicy
user_frame = ttk.LabelFrame(root, text="Użytkownicy", padding=10, style="TLabelframe")
user_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

user_id = tk.Entry(user_frame, fg='black', font=("Helvetica", 10))
user_id.grid(row=1, column=1, sticky="ew")
user_id.configure(background="white")

name = tk.Entry(user_frame, fg='black', font=("Helvetica", 10))
name.grid(row=2,column=1, sticky="ew")
name.configure(background="white")

delete_user_id = ttk.Button(user_frame, text="Usuń po id", command=lambda: delete_by_id_or_name("id"))
delete_user_id.grid(row=0, column=0, padx=5, pady=5)
delete_user_name = ttk.Button(user_frame, text="Usuń po nazwie", command=lambda: delete_by_id_or_name("name"))
delete_user_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(user_frame, text="ID klienta: ").grid(row=1, column=0, sticky="e")
tk.Label(user_frame, text="Nazwa klienta: ").grid(row=2, column=0, sticky="e")

# Dodawanie użytkownika
add_user_button = ttk.Button(user_frame, text="Dodaj użytkownika", command=add_user)
add_user_button.grid(row=3, column=0, columnspan=2, pady=5, sticky="ew")

# Dodawanie książki
add_book_button = ttk.Button(book_frame, text="Dodaj książkę", command=add_book)
add_book_button.grid(row=3, column=0, columnspan=2, pady=5, sticky="ew")

root.mainloop()
