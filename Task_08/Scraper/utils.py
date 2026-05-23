import time
import logging
import requests

logging.basicConfig(
    filename="logs/scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def retry_request(url, headers, retries=3, timeout=10):
    """
    Retry GET requests if request fails.
    """

    for attempt in range(retries):
        try:
            response = requests.get(
                url,
                headers=headers,
                timeout=timeout
            )

            if response.status_code == 200:
                return response

            logging.warning(
                f"Status Code {response.status_code} for URL: {url}"
            )

        except requests.RequestException as e:
            logging.error(f"Request failed: {e}")

        time.sleep(2)

    return None
