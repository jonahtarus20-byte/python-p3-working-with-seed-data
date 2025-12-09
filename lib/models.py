from sqlalchemy import func
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    genre = Column(String())
    platform = Column(String())
    price = Column(Integer())
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())

    def __repr__(self):
        return f'Game(id={self.id}, ' + \
            f'title="{self.title}", ' + \
            f'platform="{self.platform})"'

# Set up the engine and session
engine = create_engine('sqlite:///seed_db.db')
Session = sessionmaker(bind=engine)
session = Session()
