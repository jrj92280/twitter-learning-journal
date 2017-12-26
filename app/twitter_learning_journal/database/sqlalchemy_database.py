from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database():
    def __init__(self, database_url='data/twitter-learning-journal', *, echo=True):
        self._engine = create_engine(f'sqlite:///{database_url}', echo=echo)

        Session = sessionmaker(bind=self._engine)
        self._session = Session()

    def query(self, entity):
        return self._session.query(entity)

    def add(self, entity):
        self._session.add(entity)

    def add_all(self, entities: list):
        self._session.add_all(entities)

    def commit(self):
        self._session.commit()
