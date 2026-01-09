import requests

url = "https://openlibrary.org/search.json?q=python"  # This is an API endpoint
# This is the Open Library search API.
# q=python means we are searching for books related to Python.


# It fetches book data related to Python from an online API and returns a clean list of books with title, author, and publication year.

def get_books_from_api(limit=15):

    response = requests.get(url, timeout=10) # sends the get request to API
    response.raise_for_status() # if api fails this raise an error

    raw_data = response.json().get("docs", []) # converting API response into python dict. here we r getting docs in form of list
    
    books = [] # this is storing clear data 

    for item in raw_data[:limit]: # looping through each item in data
        title = item.get("title")
        authors = item.get("author_name", [])
        year = item.get("first_publish_year")

        books.append({
            "title": title,
            "author": authors[0] if authors else "Unknown", 
            "year": year
        })

    return books