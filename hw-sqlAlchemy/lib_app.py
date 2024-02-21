import os
from flask import Flask, render_template, url_for, request, flash
from main import menu
from queries import methods

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('base.html', menu=menu.show_menu().items())


@app.route("/show_books")
def select_books():
    return render_template('books.html', menu=menu.show_menu().items(), books=methods.select_books())


@app.route("/add_book", methods=["POST", "GET"])
def add_book():
    if request.method == "POST":
        len_authors = len(methods.select_authors())
        if len(request.form['name']) > 2 and int(request.form['id']) <= len_authors:
            methods.add_book(request.form['name'], int(request.form['id']))
            flash('Книга добавлена успешно', category='success')
        else:
            flash('Ошибка добавления книги', category='error')

    return render_template('add_book.html', menu=menu.show_menu().items(), authors=methods.select_authors())


@app.route("/add_author", methods=["POST", "GET"])
def add_author():
    if request.method == "POST":
        list_authors = [item.author_name for item in methods.select_authors()]
        if request.form['name'] in list_authors:
            flash("Такой автор уже существует", category='error')
        elif len(request.form['name']) > 1:
            methods.add_author(request.form['name'])
            flash("Автор добавлен", category='success')
        else:
            flash("Имя не может быть меньше 2 букв", category='error')
    return render_template('add_author.html', menu=menu.show_menu().items())


@app.route("/authors")
def show_authors():
    return render_template('authors.html', menu=menu.show_menu().items(), authors=methods.select_authors())


@app.route("/delete_book", methods=["POST", "GET"])
def delete_book():
    if request.method == "POST":
        if int(request.form['id']) in methods.select_book_id():
            methods.delete_book(request.form['id'])
            flash('Книга удалена', category='success')
        else:
            flash('Такой книги нет', category='error')
    return render_template('delete_book.html', menu=menu.show_menu().items(), books=methods.select_books())


@app.route('/update_book', methods=["POST", "GET"])
def update_book():
    if request.method == "POST":
        if int(request.form['id']) in methods.select_book_id():
            methods.update_book(request.form['name'], request.form['id'])
            flash('Книга изменена', category='success')
        else:
            flash('Такой книги нет', category='error')
    return render_template('update_book.html', menu=menu.show_menu().items(), books=methods.select_books())


@app.route('/search_book', methods=["POST", "GET"])
def find_book():
    book = []
    if request.method == "POST":
        book = methods.search_book(request.form['name'])
        print(book)
    return render_template('search_book.html', menu=menu.show_menu().items(), book=book)


if __name__ == '__main__':
    app.secret_key = 'sadlhasdljas'
    app.run(debug=True)
