from bs4 import BeautifulSoup
from config.settings import BASE_URL


def parse_tweets(html):
    """
    Parse tweet data from Nitter HTML.
    """

    soup = BeautifulSoup(html, "lxml")

    tweet_blocks = soup.find_all("div", class_="timeline-item")

    tweets = []

    for tweet in tweet_blocks:

        try:
            # Username
            username_tag = tweet.find("a", class_="username")
            username = username_tag.text.strip() if username_tag else "N/A"

            # Tweet Text
            text_tag = tweet.find("div", class_="tweet-content")
            text = text_tag.text.strip() if text_tag else "N/A"

            # Tweet Link
            link_tag = tweet.find("a", class_="tweet-link")
            tweet_link = (
                BASE_URL + link_tag["href"]
                if link_tag else "N/A"
            )

            # Timestamp
            time_tag = tweet.find("span", class_="tweet-date")
            timestamp = (
                time_tag.text.strip()
                if time_tag else "N/A"
            )

            # Media URL
            media_url = None

            video_tag = tweet.find("video")
            image_tag = tweet.find("img")

            if video_tag and video_tag.get("src"):
                media_url = BASE_URL + video_tag["src"]

            elif image_tag and image_tag.get("src"):
                media_url = BASE_URL + image_tag["src"]

            # Engagement Stats
            stats = tweet.find_all("span", class_="tweet-stat")

            replies = stats[0].text.strip() if len(stats) > 0 else "0"
            reposts = stats[1].text.strip() if len(stats) > 1 else "0"
            likes = stats[2].text.strip() if len(stats) > 2 else "0"

            tweets.append({
                "username": username,
                "tweet_text": text,
                "tweet_link": tweet_link,
                "media_url": media_url,
                "timestamp": timestamp,
                "replies": replies,
                "reposts": reposts,
                "likes": likes
            })

        except Exception as e:
            print(f"Parsing Error: {e}")

    return tweets
