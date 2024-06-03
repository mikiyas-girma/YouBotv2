from sqlalchemy import Column, Unicode, BigInteger
from models.engine.storage import Base


class Question(Base):
    __tablename__ = 'questions'

    question_id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, nullable=False)
    question = Column(Unicode(300), nullable=False)
    category = Column(Unicode(50), nullable=False)
    status = Column(Unicode(50), nullable=False)
    username = Column(Unicode(50), nullable=False)
    name = Column(Unicode(50), nullable=False)
    admin_message_id = Column(BigInteger, nullable=True)
    public_message_id = Column(BigInteger, nullable=True)
