from app import books

USERCHOICE = """
enter b to see best books
enter c to see cheapest books
enter n to see next available book on the catalogue
enter q to quit
"""


def print_best_books():
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10]
    for book in best_books:
        print(book)


def print_cheap_books():
    cheapestbooks = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapestbooks:
        print(book)

books_generator = (x for x in books)


def get_next_book():
    print(next(books_generator))


def menu():
    user_input = input(USERCHOICE)
    while user_input != 'q':
        if user_input == 'b':
            print_best_books()
        elif user_input == 'c':
            print_cheap_books()
        elif user_input == 'n':
            get_next_book()
        else:
            print('Invalid command. please try again')
        user_input = input(USERCHOICE)

    if user_input == 'q':
        print('Quitting...')

menu()
