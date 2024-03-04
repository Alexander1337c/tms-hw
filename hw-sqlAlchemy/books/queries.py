from db.database import create_session
from books.models import Books
from users import models

from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload


class Methods_books:

    @staticmethod
    def select_books():
        with create_session() as session:
            query = select(Books).options(joinedload(Books.authors))
            result = session.execute(query)
            books = result.scalars().all()
            return books

    @staticmethod
    def add_book(title, author_id):
        with create_session() as session:
            session.add(Books(title_book=title, author_id=author_id))
            session.flush()
            session.commit()

    @staticmethod
    def update_book(title, book_id):
        with create_session() as session:
            session.get(Books, book_id).title_book = title
            session.commit()

    @staticmethod
    def select_book_id():
        with create_session() as session:
            query = select(Books.id).select_from(Books)
            res = session.execute(query)
            result = res.scalars().all()
            return result

    @staticmethod
    def delete_book(book_id):
        with create_session() as session:
            res = session.get(Books, book_id)
            session.delete(res)
            session.commit()

    @staticmethod
    def get_book_id(book_id):
        with create_session() as session:
            res = session.get(Books, book_id)
            print(res)
            return res

    @staticmethod
    def search_book(search_str):
        with create_session() as session:
            query = select(Books).select_from(Books).where(Books.title_book.contains(search_str)).options(
                joinedload(Books.authors))
            res = session.execute(query)
            result = res.scalars().all()
            if not result:
                return [f'Book not found']
            return result

    @staticmethod
    def add_favorite(user_id, book_id):
        with create_session() as session:
            user = session.get(models.Users, user_id)
            book = session.get(Books, book_id)
            try:
                user.books_favorite.append(book)
                session.commit()
                return True
            except:
                return False

    @staticmethod
    def get_favorite_books(user_id):
        with create_session() as session:
            query = select(models.Users).filter(models.Users.id == user_id).options(
                joinedload(models.Users.books_favorite).options(joinedload(Books.authors)))
            res = session.execute(query)
            books_favorite = res.scalars().unique().all()
            list_books = books_favorite[0].books_favorite
            return list_books


methods = Methods_books()
