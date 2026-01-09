from api import get_books_from_api
from database import database_setup, save_books, read_books


def execute_pipeline():

    database_setup()

    books = get_books_from_api()

    save_books(books)

    stored_books = read_books()
    for book in stored_books:
        print(book)

if __name__ == "__main__":
    execute_pipeline()
