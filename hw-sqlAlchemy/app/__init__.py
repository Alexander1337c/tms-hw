from flask import Flask
from db.config import settings

app = Flask(__name__)
print(settings)
app.config['SECRET_KEY'] = settings.SECRET_KEY

from app.routes import *

from books import books

app.register_blueprint(books, url_prefix='/books')

from authors import authors

app.register_blueprint(authors, url_prefix='/authors')

from users import users

app.register_blueprint(users, url_prefix='/users')
