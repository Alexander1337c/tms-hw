from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfh12u3124j5'

from app.routes import *

from books import books

app.register_blueprint(books, url_prefix='/books')

from authors import authors

app.register_blueprint(authors, url_prefix='/authors')

from users import users

app.register_blueprint(users, url_prefix='/users')