from create_tables import Tables
from queries import Methods


class Menu:
    def __init__(self, rep_of_method):
        self.list_menu = [
            "Show Books",
            "Add Book",
            "Update Book",
            "Delete Book",
            "Show Authors",
            "Add Author",
            "Find Book",
            "Exit"
        ]
        self.methods = rep_of_method
        self.wrapper_method = [
            self.inner_select_books,
            self.inner_add_book,
            self.inner_update_book,
            self.inner_delete_book,
            self.inner_select_authors,
            self.inner_add_author,
            self.inner_search_book,
            self.exit_fn
        ]

    def show_menu(self):
        print(*enumerate(self.list_menu, start=1), sep='\n')
        user_input = int(input('Choose an action '))
        if not isinstance(user_input, int) and user_input > len(self.list_menu):
            raise ValueError('Your choice must be integer')
        method = self.pick_menu(user_input)
        return method()

    def pick_menu(self, item):
        return self.wrapper_method[item - 1]

    def inner_select_books(self):
        self.methods.select_books()

    def inner_add_book(self):
        user_input_title = input('Enter the book title: ')
        user_input_id = int(input('Enter the author_id(integer): '))
        len_authors = len(self.methods.select_authors())
        if user_input_id > len_authors:
            raise ValueError('No such author exists')
        self.methods.add_book(user_input_title, user_input_id)

    def inner_update_book(self):
        user_input_title = input('Enter the new book title: ')
        user_input_id = int(input('Enter the book_id(integer): '))
        if user_input_id not in self.methods.select_book_id():
            raise ValueError('No such book exists')
        self.methods.update_book(user_input_title, user_input_id)

    def inner_delete_book(self):
        user_input_id = int(input('Enter the book_id(integer): '))
        if user_input_id not in self.methods.select_book_id():
            raise ValueError('No such book exists')
        self.methods.delete_book(user_input_id)

    def inner_select_authors(self):
        self.methods.select_authors()

    def inner_add_author(self):
        user_input = input('Enter the new Author: ')
        self.methods.add_author(user_input)

    def inner_search_book(self):
        user_input = input('Search input: ')
        self.methods.search_book(user_input)

    def exit_fn(self):
        return False


if __name__ == '__main__':
    # Создаем таблицы авторов и книг
    # Tables.create_tables()

    # Добавляем данные в таблицы
    # Tables.insert_authors_and_books()

    a = Menu(Methods)
    while True:
        try:
            if a.show_menu() == False:
                break
            a.show_menu()
        except Exception as e:
            print(e)

