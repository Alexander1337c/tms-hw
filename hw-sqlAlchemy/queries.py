from sqlalchemy import select
from sqlalchemy.orm import joinedload
from database import create_session
from models import Authors, Books


class Methods:

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
    def select_authors():
        with create_session() as session:
            query = select(Authors)
            res = session.execute(query)
            authors = res.scalars().all()
            return authors

    @staticmethod
    def add_author(name):
        with create_session() as session:
            session.add(Authors(author_name=name))
            session.flush()
            session.commit()

    @staticmethod
    def search_book(search_str):
        with create_session() as session:
            query = select(Books).select_from(Books).where(Books.title_book.contains(search_str)).options(joinedload(Books.authors))
            res = session.execute(query)
            result = res.scalars().all()
            if not result:
                return [f'Book not found']
            return result


methods = Methods()
