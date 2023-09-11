import os
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, orm

root_path = os.path.dirname(os.path.realpath(__file__))
db_uri = os.path.join(root_path, 'db.db')
engine = create_engine(f'sqlite:///{db_uri}', echo=True)


base = sqlalchemy.orm.declarative_base()
base.metadata.create_all(bind=engine)
class users(base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)


