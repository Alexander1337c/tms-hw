from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base
from authors import models

class Books(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title_book: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id", ondelete="CASCADE"))

    authors: Mapped["models.Authors"] = relationship(back_populates="books")

    def __str__(self):
        return f'{self.id}. {self.title_book}: {self.authors}'

    def __repr__(self):
        return str(self)