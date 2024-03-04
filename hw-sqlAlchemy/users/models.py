from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.database import Base
from books.models import Books


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]

    books_favorite: Mapped[list['Books']] = relationship(
        back_populates='users_favorite',
        secondary='favorite_books'
    )

    def __str__(self):
        return f'{self.id, self.name, self.email}'

    def __repr__(self):
        return str(self)
