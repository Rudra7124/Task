import os

# Ensure the 'data' directory exists
os.makedirs('data', exist_ok=True)

# Keywords from the previously defined SEARCH_KEYWORDS variable
search_keywords_list = [
    "AI generated videos",
    "Robotics demos",
    "Self-driving cars",
    "Sports highlights"
]

# Write the keywords to data/keywords.txt with a default category
with open('data/keywords.txt', 'w', encoding='utf-8') as f:
    for keyword in search_keywords_list:
        f.write(f"general: {keyword}\n")

print("Created data/keywords.txt with initial keywords.")
