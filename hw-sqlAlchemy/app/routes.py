from app import app
from flask import render_template

menu = [{'url': 'books.select_books', 'title': 'Книги'}, {'url': 'authors.index', 'title': 'Авторы'}]

@app.route("/")
def index():
    return render_template("base/base.html", menu=menu, title='Главная страница')
