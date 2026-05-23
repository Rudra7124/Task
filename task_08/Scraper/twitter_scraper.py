import urllib.parse


def search_tweets(keyword):

    encoded_keyword = urllib.parse.quote(keyword)

    url = f"{BASE_URL}/search?f=tweets&q={encoded_keyword}"

    response = retry_request(
        url,
        headers=HEADERS,
        retries=RETRY_COUNT,
        timeout=REQUEST_TIMEOUT
    )

    if not response:
        print(f"Failed to fetch tweets for: {keyword}")
        return []

    tweets = parse_tweets(response.text)

    tweets = tweets[:MAX_TWEETS]

    # Download media
    for tweet in tweets:

        media_path = download_media(tweet["media_url"])

        tweet["downloaded_media"] = media_path

    return tweets
