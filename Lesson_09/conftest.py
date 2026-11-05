import pytest
from sqlalchemy import create_engine


DATABASE_URL = "postgresql://postgres:132666@localhost:5432/Tables_final"


@pytest.fixture(scope="session")
def engine():
    return create_engine(DATABASE_URL, echo=False)


@pytest.fixture
def db_conn(engine):
    # открываем соединение с базой
    connection = engine.connect()
    transaction = connection.begin()

    yield connection

    # откатываем транзакцию — все данные теста пропадают
    transaction.rollback()
    connection.close()
