from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from db.config import settings

engine = create_engine(
    url=settings.DATABASE_URL,
    echo=False,
)

create_session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass
