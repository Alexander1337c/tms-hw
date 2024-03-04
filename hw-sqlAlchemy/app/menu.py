
class Menu:
    def __init__(self):
        self.list_menu = {
            "books.select_books": "Показать книги",
            "books.add_book": "Add Book",
            "books.update_book": "Update Book",
            "books.delete_book": "Delete Book",
            "authors.show_authors": "Show Authors",
            "authors.add_author": "Add Author",
            "books.find_book": "Find Book",
        }

    def show_menu(self):
        return self.list_menu


menu = Menu()

