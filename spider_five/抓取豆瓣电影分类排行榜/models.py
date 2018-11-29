#encoding: utf-8

from spider_five.抓取豆瓣电影分类排行榜.config import Base, db_session
from sqlalchemy import Column, String, Integer, Boolean, DateTime


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    image = Column(String(100), nullable=True)
    is_playable = Column(Boolean)
    types = Column(String(100))
    regions = Column(String(100))
    release_date = Column(String(50))


if __name__ == '__main__':
    Base.metadata.drop_all()
    Base.metadata.create_all()