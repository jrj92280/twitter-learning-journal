from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.twitter_learning_journal.models import Base
from app.twitter_learning_journal.models.detail import Detail
from app.twitter_learning_journal.models.tweet_raw_data import TweetRawData


class Tweet(Base):
    __tablename__ = 'tweet'

    id = Column(Integer, primary_key=True)

    details = relationship(Detail, back_populates='tweet')
    tweet_raw_data = relationship(TweetRawData, back_populates='tweet')

    screen_name = Column(String)
    created_at = Column(DateTime)
    full_text = Column(String)
    hashtags = Column(String)
    urls = Column(String)
    type = Column(String)
    count = Column(Integer, default=0)
    classification = Column(String)
    is_fully_classified = Column(Boolean, default=False)

    def __str__(self):
        return f'<Tweet(id={self.id}, ' \
               f'screen_name={self.screen_name}, ' \
               f'created_at={self.created_at}, ' \
               f'full_text={self.full_text}, ' \
               f'type={self.type}, ' \
               f'hashtags={self.hashtags}, ' \
               f'urls={self.urls}, ' \
               f'count={self.count}, ' \
               f'classification={self.classification})>'

    def __eq__(self, other):
        equal = self.created_at == other.created_at \
                and self.full_text == other.full_text \
                and self.type == other.type \
                and self.hashtags == other.hashtags

        return equal
