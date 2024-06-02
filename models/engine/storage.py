from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os


DB_URL = 'mysql+mysqldb://mike:Mm001122@localhost/youbotdb'

engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def init_db():
    from models import question, answer, user, asked, user_reaction
    Base.metadata.create_all(bind=engine)
    return engine
