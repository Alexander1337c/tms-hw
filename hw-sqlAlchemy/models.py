from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Authors(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    author_name: Mapped[str]

    books: Mapped[list["Books"]] = relationship(
        back_populates="authors"
    )

    def __str__(self):
        return f'<Author>: {self.id}. {self.author_name}'


class Books(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title_book: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id", ondelete="CASCADE"))

    authors: Mapped["Authors"] = relationship(back_populates="books", )

    def __str__(self):
        return f'{self.id}. {self.title_book}: {self.authors}'

    def __repr__(self):
        return str(self)
