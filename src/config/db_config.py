from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .settings import Settings

DB_URL = f"postgresql://{Settings().DB_USER}:{Settings().DB_PASSWORD}@{Settings().DB_HOST}:{Settings().DB_PORT}/{Settings().DB_NAME}"

Base = declarative_base()

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
