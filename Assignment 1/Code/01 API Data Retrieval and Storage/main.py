from api import get_books_from_api
from database import database_setup, save_books, read_books


def execute_pipeline():

    database_setup() # calling database setup like all methods to do database operations

    books = get_books_from_api() # getting data from api which has not any api key open for all

    save_books(books) # inserted books data into table

    stored_books = read_books() # read and print data 
    for book in stored_books:
        print(book)

if __name__ == "__main__": # this means Run execute_pipeline() only when the main file is run, not when it’s imported
    execute_pipeline()
