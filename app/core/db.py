from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

from core.config import settings


class Base(DeclarativeBase):
    pass


engine = create_engine(
    url=settings.DB_URL,
    echo=True,
)


SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_session() -> Generator[Session, None, None]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
