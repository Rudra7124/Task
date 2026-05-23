import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Load dataset
df = pd.read_csv("/content/output/tweets.csv")

# -----------------------------
# Basic Analysis
# -----------------------------

# Total videos collected
total_videos = len(df)

# Total unique creators
total_creators = df['username'].nunique()

# Most common keywords
all_keywords = " ".join(df['tweet_text'].astype(str)).lower().split()
common_keywords = Counter(all_keywords).most_common(10)

# Average engagement statistics
avg_likes = df['likes'].mean()
avg_reposts = df['reposts'].mean()

# Top-performing posts
top_posts = df.sort_values(by='likes', ascending=False).head(5)

# -----------------------------
# Save Summary Report
# -----------------------------

with open("summary_report.txt", "w", encoding="utf-8") as file:
    file.write("DATA SUMMARY REPORT\n")
    file.write("====================\n\n")

    file.write(f"Total Videos Collected: {total_videos}\n")
    file.write(f"Total Unique Creators: {total_creators}\n\n")

    file.write("Most Common Keywords:\n")
    for word, count in common_keywords:
        file.write(f"{word}: {count}\n")

    file.write("\nAverage Engagement Statistics:\n")
    file.write(f"Average Likes: {avg_likes:.2f}\n")
    file.write(f"Average Reposts: {avg_reposts:.2f}\n\n")

    file.write("Top Performing Posts:\n")
    for index, row in top_posts.iterrows():
        file.write(f"\nUsername: {row['username']}\n")
        file.write(f"Tweet: {row['tweet_text']}\n")
        file.write(f"Likes: {row['likes']}\n")
        file.write(f"Reposts: {row['reposts']}\n")

print("Summary report saved as summary_report.txt")

# -----------------------------
# Visualization 1
# Top 10 Common Keywords
# -----------------------------

keywords = [word for word, count in common_keywords]
counts = [count for word, count in common_keywords]

plt.figure(figsize=(10,5))
plt.bar(keywords, counts)
plt.title("Top 10 Common Keywords")
plt.xlabel("Keywords")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# Visualization 2
# Engagement Statistics
# -----------------------------

engagement = ['Average Likes', 'Average Reposts']
values = [avg_likes, avg_reposts]

plt.figure(figsize=(6,5))
plt.bar(engagement, values)
plt.title("Average Engagement Statistics")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
