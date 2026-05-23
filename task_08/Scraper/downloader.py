import os
import requests


def download_media(media_url, output_folder="output/media"):
    """
    Download media if available.
    """

    if not media_url:
        return None

    try:
        os.makedirs(output_folder, exist_ok=True)

        filename = media_url.split("/")[-1].split("?")[0]

        filepath = os.path.join(output_folder, filename)

        response = requests.get(media_url, stream=True)

        if response.status_code == 200:

            with open(filepath, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)

            return filepath

    except Exception as e:
        print(f"Download Error: {e}")

    return None
