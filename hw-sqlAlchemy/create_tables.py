from sqlalchemy import insert
from database import engine, create_session, Base
from models import Authors, Books


class Tables:
    @staticmethod
    def create_tables():
        Base.metadata.drop_all(engine)
        engine.echo = False
        Base.metadata.create_all(engine)
        engine.echo = False

    @staticmethod
    def insert_authors_and_books():
        with create_session() as session:
            authors = [
                {"author_name": "Lermontov"},
                {"author_name": "Pushkin"},
                {"author_name": "Dostoevskiy"},
                {"author_name": "Bulgakov"},
            ]

            books = [
                {"title_book": "Prorok", "author_id": 2},
                {"title_book": "Dubrovskiy", "author_id": 2},
                {"title_book": "Parus", "author_id": 1},
                {"title_book": "Duma", "author_id": 1},
                {"title_book": "Belye Nochi", "author_id": 3},
                {"title_book": "Sobach`e serdce", "author_id": 4},
                {"title_book": "Dvoinik", "author_id": 3},
                {"title_book": "Master i Margarita", "author_id": 4},
            ]
            insert_authors = insert(Authors).values(authors)
            insert_books = insert(Books).values(books)

            session.execute(insert_authors)
            session.execute(insert_books)
            session.commit()
