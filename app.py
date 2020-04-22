import requests
from pages.all_books_page import Allbookspage


page_content = requests.get('http://books.toscrape.com/').content
page = Allbookspage(page_content)

books = page.books

if __name__ == 'main':
    for book in books:
        print(book)

