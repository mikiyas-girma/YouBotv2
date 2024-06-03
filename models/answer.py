from sqlalchemy import Column, String, BigInteger, ForeignKey, Unicode
from models.engine.storage import Base


class Answer(Base):
    __tablename__ = 'answers'

    answer_id = Column(BigInteger, primary_key=True)
    question_id = Column(BigInteger, nullable=False)
    user_id = Column(BigInteger, nullable=False)
    chat_id = Column(BigInteger, nullable=False)
    username = Column(Unicode(50), nullable=False)
    answer = Column(Unicode(50), nullable=False)
    status = Column(String(50), nullable=False)
    likes = Column(BigInteger, nullable=True, default=0)
    dislikes = Column(BigInteger, nullable=True, default=0)
    reputation = Column(BigInteger, nullable=True)
    reply_to = Column(BigInteger, ForeignKey('answers.answer_id'),
                      nullable=True)
    tg_msg_id = Column(BigInteger, nullable=True)
