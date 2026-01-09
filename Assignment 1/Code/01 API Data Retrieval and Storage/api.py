import requests

url = "https://openlibrary.org/search.json?q=python"


def get_books_from_api(limit=15):

    response = requests.get(url, timeout=10)
    response.raise_for_status() 

    raw_data = response.json().get("docs", []) 
    
    books = []

    for item in raw_data[:limit]:
        title = item.get("title")
        authors = item.get("author_name", [])
        year = item.get("first_publish_year")

        books.append({
            "title": title,
            "author": authors[0] if authors else "Unknown", 
            "year": year
        })

    return books