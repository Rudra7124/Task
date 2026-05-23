import urllib.parse

from config.settings import (
    BASE_URL,
    HEADERS,
    RETRY_COUNT,
    REQUEST_TIMEOUT,
    MAX_TWEETS_PER_KEYWORD
)

from scraper.utils import retry_request
from scraper.parser import parse_tweets
from scraper.downloader import download_media


def search_tweets(keyword, category):

    encoded_keyword = urllib.parse.quote(keyword)

    url = f"{BASE_URL}/search?f=tweets&q={encoded_keyword}"

    response = retry_request(
        url,
        headers=HEADERS,
        retries=RETRY_COUNT,
        timeout=REQUEST_TIMEOUT
    )

    if not response:
        return []

    tweets = parse_tweets(response.text)

    tweets = tweets[:MAX_TWEETS_PER_KEYWORD]

    collected = []

    for tweet in tweets:

        tweet["category"] = category
        tweet["search_keyword"] = keyword

        media_path = download_media(
            tweet["media_url"],
            category
        )

        tweet["downloaded_media"] = media_path

        collected.append(tweet)

    return collected
