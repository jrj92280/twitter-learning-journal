from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.twitter_learning_journal.models import Base


class Detail(Base):
    __tablename__ = 'detail'

    id = Column(Integer, primary_key=True)

    tweet_id = Column(Integer, ForeignKey('tweet.id'))
    tweet = relationship('Tweet', back_populates='details')

    start_date = Column(DateTime)
    stop_date = Column(DateTime)
    type = Column(String)
    title = Column(String)
    classification = Column(String)

    def __str__(self):
        return f'<Detail(id={self.id}, ' \
               f'tweet_id={self.tweet_id}, ' \
               f'start_date={self.start_date}, ' \
               f'stop_date={self.stop_date}, ' \
               f'type={self.type}, ' \
               f'title={self.title}, ' \
               f'classification={self.classification})>'

    def __eq__(self, other):
        return self.id == other.id
