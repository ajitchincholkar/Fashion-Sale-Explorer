from time import sleep
import requests
from backend.utils import log_config

# Set up logging
log_config.setup_logging()

# Create a logger for uniqlo_scraper.py
logger = log_config.get_logger(__name__)

# Define user-agent header for the HTTP request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}


def scrape_uniqlo():
    logger.info("Inside scrape_uniqlo() function...")
    offset = 0
    total = 0

    uniqlo_raw = []

    while offset <= total:
        response = requests.get(
            f'https://www.uniqlo.com/in/api/commerce/v3/en/products?path=9672&flagCodes=discount%2Cdiscount&limit=50&offset={offset}',
            headers=headers)
        sleep(2)
        data = response.json()

        uniqlo_raw.append(data['result']['items'])

        offset = data['result']['pagination']['offset']
        total = data['result']['pagination']['total']

    return uniqlo_raw
