from app import app
from flask import render_template, session, g
from users.queries import methods

menu = [{'url': 'books.select_books', 'title': 'Книги'}, {'url': 'authors.index', 'title': 'Авторы'}]


@app.before_request
def load_user():
    if "user" in session:
        user_id = session.get("user")
        g.user = methods.get_user_id(user_id)
    else:
        g.user = None



@app.route("/")
def index_app():
    return render_template("base/base.html", menu=menu, title='Главная страница', user=g.user)
