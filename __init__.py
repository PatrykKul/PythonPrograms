'''
Module: Customer_Service

Description:
The Customer_Service module provides functions for managing customers, including adding, deleting, and borrowing and returning books.

Functions:

1. add_client():
    Description: Adds a new client to the customer database and their address to the address database.
    Parameters:
        None.
    Returns:
        None.

2. delete_client_by_id(id):
    Description: Deletes a client from the database based on their ID.
    Parameters:
        id (int): The ID of the client to be deleted.
    Returns:
        None.

3. delete_client_by_name(name):
    Description: Deletes a client from the database based on their name.
    Parameters:
        name (str): The name of the client to be deleted.
    Returns:
        None.

4. borrow_book(client_id, book_id):
    Description: Borrows a book for a specified client and adds borrowing information to the client's file.
    Parameters:
        client_id (int): The ID of the client for whom the book is being borrowed.
        book_id (int): The ID of the book being borrowed.
    Returns:
        None.

5. return_book(client_id, book_id, multiple=False):
    Description: Returns a borrowed book to the library and updates information in the client's file.
    Parameters:
        client_id (int): The ID of the client returning the book.
        book_id (int): The ID of the book being returned.
        multiple (bool, optional): A flag indicating whether multiple books are being returned (default is False).
    Returns:
        None.

    Returns:
    None.

'''