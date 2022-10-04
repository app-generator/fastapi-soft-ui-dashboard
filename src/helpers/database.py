from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLITE_DATABASE_URL = "sqlite:///./src/sql_app.db"

engine = create_engine(SQLITE_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
