from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base
from books import models


class Authors(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    author_name: Mapped[str]

    books: Mapped[list["models.Books"]] = relationship(
        back_populates="authors"
    )

    def __str__(self):
        return f'{self.author_name}'

    def __repr__(self):
        return str(self)