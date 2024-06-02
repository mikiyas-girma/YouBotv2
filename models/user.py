from datetime import datetime
from sqlalchemy import Column, Date, Integer, String, BigInteger
from models.engine.storage import Base


class User(Base):
    __tablename__ = 'users'
    telegram_id = Column(BigInteger, primary_key=True, unique=True,
                         nullable=False)
    name = Column(String(255), nullable=False, default='Anonymous')
    username = Column(String(255), unique=True, index=True)
    gender = Column(String(255), default=None)
    bio = Column(String(255), default='You don''t have a bio yet.')
    reputation = Column(Integer, default=0)
    followers = Column(String(255), default='')
    following = Column(String(255), default='')
    date_joined = Column(Date, default=datetime.now().date())
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
