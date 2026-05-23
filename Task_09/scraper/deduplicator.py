def remove_duplicates(tweets):
    """
    Remove duplicate tweets based on:
    - tweet_link
    - media_url
    """

    unique = {}
    
    for tweet in tweets:

        unique_key = (
            tweet.get("tweet_link"),
            tweet.get("media_url")
        )

        if unique_key not in unique:
            unique[unique_key] = tweet

    return list(unique.values())
