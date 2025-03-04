from sqlalchemy import create_engine
from sqlalchemy import Session
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

from core.config import settings


class Base(DeclarativeBase):
    pass


engine = create_engine(url=settings.DB_URL, echo=True)


session_factory = sessionmaker(engine, class_=Session, expire_on_commit=False)


def get_session() -> Session:
    with session_factory() as session:
        yield session
