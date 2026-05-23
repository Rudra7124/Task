import os
import json
import pandas as pd


def save_json(data, filepath):

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def save_csv(data, filepath):

    df = pd.DataFrame(data)

    df.to_csv(filepath, index=False)


def main():

    os.makedirs("output", exist_ok=True)

    all_tweets = []

    for keyword in SEARCH_KEYWORDS:

        print(f"\nSearching for: {keyword}")

        tweets = search_tweets(keyword)

        all_tweets.extend(tweets)

    # Save JSON
    save_json(all_tweets, "output/tweets.json")

    # Save CSV
    save_csv(all_tweets, "output/tweets.csv")

    print("\nScraping Completed Successfully!")
    print(f"Total Tweets Collected: {len(all_tweets)}")


if __name__ == "__main__":
    main()
