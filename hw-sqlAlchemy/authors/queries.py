from db.database import create_session
from .models import Authors

from sqlalchemy import select
from sqlalchemy.orm import joinedload


class Methods_authors:
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


methods = Methods_authors()
