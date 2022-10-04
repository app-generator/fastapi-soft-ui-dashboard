import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.app import app as root_app
from src.helpers.database import get_db, Base


SQLITE_DATABASE_URL = 'sqlite:///./sql_app_test.db'

engine = create_engine(SQLITE_DATABASE_URL, connect_args={'check_same_thread': False})

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    root_app.dependency_overrides[get_db] = override_get_db
    yield TestClient(root_app)