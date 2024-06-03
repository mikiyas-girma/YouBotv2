from sqlalchemy import Column, String, BigInteger, Unicode
from models.engine.storage import Base


class Asked(Base):
    __tablename__ = 'asked'

    question_id = Column(BigInteger, primary_key=True)
    user_question = Column(Unicode(300))
    question_category = Column(Unicode(300))
    preview_message_id = Column(BigInteger)
