def load_keywords(filepath):
    """
    Load keywords and categories from file.
    """

    keyword_map = {}

    with open(filepath, "r", encoding="utf-8") as file:

        for line in file:

            line = line.strip()

            if not line or ":" not in line:
                continue

            category, keyword = line.split(":", 1)

            category = category.strip().lower()
            keyword = keyword.strip()

            if category not in keyword_map:
                keyword_map[category] = []

            keyword_map[category].append(keyword)

    return keyword_map
