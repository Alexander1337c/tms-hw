from flask import Blueprint

books = Blueprint('books', __name__, template_folder='templates', static_folder='static')

from books.routes import *