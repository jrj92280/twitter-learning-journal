from datetime import datetime
from unittest.mock import MagicMock, patch

from pytest import fixture

from app.twitter_learning_journal.models.tweet import Tweet
from app.twitter_learning_journal.twitter_api.tweets import Tweets


@fixture(name='tweets')
def _tweets():
    mock_twitter_api = MagicMock()
    tweets = Tweets(mock_twitter_api, 'screen_name')

    assert tweets
    assert mock_twitter_api == tweets._twitter_api
    assert 'screen_name' == tweets.screen_name

    return tweets


@patch('app.twitter_learning_journal.twitter_api.tweets.Cursor')
def test_call(mock_cursor, tweets):
    mock_cursor.return_value.items.return_value = ['1']

    generator_response = tweets._call()
    items = [item for item in generator_response]

    assert "<class 'generator'>" == str(type(generator_response))
    assert ['1'] == items
    assert mock_cursor.called
    mock_cursor.assert_called_with(tweets._twitter_api.favorites, 'screen_name', count=200, tweet_mode='extended')


@patch('app.twitter_learning_journal.twitter_api.tweets.Tweets._call')
def test_get(mock_call, tweets):
    id = 1
    created_at = datetime.now()
    full_text = 'full_text'
    entities = {
        'hashtags': [
            {
                'text': 'some_text'
            },
            {
                'text': 'other_text'
            }
        ]
    }

    tweet_response = MagicMock(id=id,
                               created_at=created_at,
                               full_text=full_text,
                               entities=entities)
    delattr(tweet_response, 'retweeted_status')
    mock_call.return_value = [tweet_response]

    expected_tweet_model = Tweet(
        id=id,
        created_at=created_at,
        full_text=full_text,
        hashtags='some_text|other_text',
        type='favorite'
    )

    tweets_list = tweets.get()

    assert [expected_tweet_model] == tweets_list
    assert mock_call.called


@patch('app.twitter_learning_journal.twitter_api.tweets.Tweets.extract_hashtags')
@patch('app.twitter_learning_journal.twitter_api.tweets.Tweets._call')
def test_get_with_retweeted_status(mock_call, mock_extract_hashtags, tweets):
    full_text = 'full_text'

    tweet_response = MagicMock(id=id, retweeted_status=MagicMock(full_text=full_text))
    mock_call.return_value = [tweet_response]

    expected_tweet_model = Tweet(
        id=tweet_response.id,
        created_at=tweet_response.created_at,
        full_text=full_text,
        type='favorite',
        hashtags=mock_extract_hashtags.return_value
    )

    tweets_list = tweets.get()

    assert [expected_tweet_model] == tweets_list
    assert mock_call.called