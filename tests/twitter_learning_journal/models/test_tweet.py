from datetime import datetime

from app.twitter_learning_journal.models.tweet import Tweet


def test_tweet():
    created_at = datetime.now()
    full_text = 'full_text'
    _type = 'type'
    hashtags = 'hashtags'
    urls = None
    word_count = 0
    classification = 'classification'

    expected_raw_data = b'raw_data'
    expected_str = '<Tweet(id=1, ' \
                   f'created_at={created_at}, ' \
                   f'full_text={full_text}, ' \
                   f'type={_type}, ' \
                   f'hashtags={hashtags}, ' \
                   f'urls={urls}, ' \
                   f'word_count={word_count}, ' \
                   f'classification={classification})>'

    tweet = Tweet(
        id=1,
        created_at=created_at,
        full_text=full_text,
        hashtags=hashtags,
        type=_type,
        word_count=word_count,
        classification=classification,
        raw_data=expected_raw_data
    )

    assert [] == tweet.details
    assert 0 == tweet.word_count
    assert None == tweet.is_fully_classified
    assert expected_raw_data == tweet.raw_data
    assert expected_str == str(tweet)
