from books import books
from .queries import methods
from flask import render_template, request, flash, url_for, g
from app import routes
from authors import queries

menu_books = [{'url': '.add_book', 'title': 'Добавить книгу'}, {'url': '.delete_book', 'title': 'Удалить книгу'},
              {'url': '.update_book', 'title': 'Изменить книгу'}, {'url': '.find_book', 'title': 'Найти книгу'}]


@books.route("/")
def select_books():
    return render_template('books/books.html', books=methods.select_books(), menu=routes.menu, menu_total=menu_books)


@books.route('/<int:book_id>', methods=['GET', 'POST'])
def book_detail(book_id):
    total_page = len(methods.select_books())

    return render_template('books/book.html', menu=routes.menu, menu_total=menu_books,
                           book=methods.get_book_id(book_id),
                           total_page=total_page)


@books.route("/add_book", methods=["POST", "GET"])
def add_book():
    if request.method == "POST":
        len_authors = len(queries.methods.select_authors())
        if len(request.form['name']) > 2 and int(request.form['id']) <= len_authors:
            methods.add_book(request.form['name'], int(request.form['id']))
            flash('Книга добавлена успешно', category='success')
        else:
            flash('Ошибка добавления книги', category='error')

    return render_template('books/add_book.html', menu=routes.menu, menu_total=menu_books)


@books.route("/delete_book", methods=["POST", "GET"])
def delete_book():
    if request.method == "POST":
        if int(request.form['id']) in methods.select_book_id():
            methods.delete_book(request.form['id'])
            flash('Книга удалена', category='success')
        else:
            flash('Такой книги нет', category='error')
    return render_template('books/delete_book.html', menu=routes.menu, menu_total=menu_books,
                           books=methods.select_books())


@books.route('/update_book', methods=["POST", "GET"])
def update_book():
    if request.method == "POST":
        if int(request.form['id']) in methods.select_book_id():
            methods.update_book(request.form['name'], request.form['id'])
            flash('Книга изменена', category='success')
        else:
            flash('Такой книги нет', category='error')
    return render_template('books/update_book.html', menu=routes.menu, menu_total=menu_books,
                           books=methods.select_books())


@books.route('/search_book', methods=["POST", "GET"])
def find_book():
    book = []
    if request.method == "POST":
        book = methods.search_book(request.form['name'])
        print(book)
    return render_template('books/search_book.html', menu=routes.menu, menu_total=menu_books, book=book)


@books.route('/add_favorite/<int:book_id>', methods=["POST", "GET"])
def add_favorite(book_id):
    if g.user:
        if not methods.add_favorite(g.user.id, book_id):
            flash('Такая книга уже есть в избранном', category='error')
        else:
            flash('Книга добавлена в избранное', category='success')
    else:
        flash('Добалвять могут только авторизированные пользователи', category='error')
    return render_template('books/books.html', menu=routes.menu, menu_total=menu_books,
                           books=methods.select_books())


@books.route('/delete_favorite/<int:book_id>', methods=["POST", "GET"])
def delete_favorite(book_id):
    if g.user:
        flash('Книга удалена', category='success')
        methods.delete_favorite_book(g.user.id, book_id)
    return render_template('books/favorite.html', menu=routes.menu, menu_total=menu_books,
                           books=methods.get_favorite_books(g.user.id))


@books.route('/favorite', methods=["POST", "GET"])
def favorite():
    return render_template('books/favorite.html', menu=routes.menu, menu_total=menu_books,
                           books=methods.get_favorite_books(g.user.id))
