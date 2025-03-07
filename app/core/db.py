from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


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
