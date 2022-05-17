from sqlalchemy import Column, DateTime, Integer, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Post(Base):

    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    rubrics = Column(Text)
    text = Column(Text)
    created_date = Column(DateTime)
