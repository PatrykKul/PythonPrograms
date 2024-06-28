from Obsluga_Ksiazek import *
from Obsluga_Klienta import *
def delete_books(fun, **kwargs):
    if 'id' in kwargs:
        fun(kwargs['id'])
    elif 'title' in kwargs:
        fun(kwargs['title'])

def delete_clients(fun,**kwargs):
    if 'id' in kwargs:
        fun(kwargs['id'])
    elif 'name' in kwargs:
        fun(kwargs['name'])