from locators.all_books_page import AllbookspageLocators
from parsers.book import BookParser
from bs4 import BeautifulSoup


class Allbookspage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(AllbookspageLocators.BOOKS)]
