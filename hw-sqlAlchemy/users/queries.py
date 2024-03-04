from db.database import create_session
from users.models import Users

from sqlalchemy import select
from sqlalchemy.orm import joinedload


class Methods_users:

    @staticmethod
    def select_users():
        with create_session() as session:
            query = select(Users)
            result = session.execute(query)
            users = result.scalars().all()
            return users

    @staticmethod
    def get_user_id(_id):
        with create_session() as session:
            user = session.get(Users, _id)
            return user

    @staticmethod
    def select_email_user(email):
        with create_session() as session:
            query = select(Users).filter(Users.email == email)
            result = session.execute(query)
            user = result.scalars().one_or_none()
            return user

    @staticmethod
    def add_user(name, email, password):
        with create_session() as session:
            session.add(Users(name=name, email=email, password=password))
            session.flush()
            session.commit()


methods = Methods_users()
