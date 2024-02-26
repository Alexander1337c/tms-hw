from authors import authors
from .queries import methods
from flask import render_template, request, flash
from app.routes import menu

menu_authors = [{'url': '.add_author', 'title': 'Добавить автора'}, {'url': 'authors.index', 'title': 'Авторы'}]

@authors.route("/")
def index():
    return render_template('authors/authors.html', authors=methods.select_authors(), menu=menu, menu_total=menu_authors)

@authors.route("/add_author", methods=["POST", "GET"])
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
    return render_template('authors/add_author.html', menu=menu, menu_total=menu_authors)



