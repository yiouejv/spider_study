#encoding: utf-8
from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

HOST = '127.0.0.1'
PORT = 3306
DATABASE = 'spiderdb'
USERNAME = 'root'
PASSWORD = 123456

DB_URL = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}".format(
    username=USERNAME, password=PASSWORD, host=HOST, port=PORT, db=DATABASE
)
engine = create_engine(DB_URL)

Base = declarative_base(engine)
session = sessionmaker(engine)()


class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    star = Column(String(100), nullable=False)
    time = Column(String(20))


Base.metadata.drop_all()
Base.metadata.create_all()