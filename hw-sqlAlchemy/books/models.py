from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base
from authors import models
from users import models


class Books(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title_book: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id", ondelete="CASCADE"))

    authors: Mapped["models.Authors"] = relationship(back_populates="books")

    users_favorite: Mapped[list['models.Users']] = relationship(
        back_populates='books_favorite',
        secondary='favorite_books'
    )

    def __str__(self):
        return f'{self.id}. {self.title_book}: {self.authors}'

    def __repr__(self):
        return str(self)


class FavoriteUsersBook(Base):
    __tablename__ = "favorite_books"

    book_id: Mapped[int] = mapped_column(
        ForeignKey('books.id', ondelete='CASCADE'),
        primary_key=True,
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'),
        primary_key=True,
    )
