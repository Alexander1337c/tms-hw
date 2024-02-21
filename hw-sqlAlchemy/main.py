from create_tables import Tables
from queries import Methods


class Menu:
    def __init__(self, rep_of_method):
        self.list_menu = {
            "select_books": "Show Books",
            "add_book": "Add Book",
            "update_book": "Update Book",
            "delete_book": "Delete Book",
            "show_authors": "Show Authors",
            "add_author": "Add Author",
            "find_book": "Find Book",
        }

    def show_menu(self):
        return self.list_menu


menu = Menu(Methods)
