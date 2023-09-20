import requests
import pandas as pd
import json
from backend.utils import log_config

# Set up logging
log_config.setup_logging()

# Create a logger for zara_scraper.py
logger = log_config.get_logger(__name__)

# Define user-agent header for the HTTP request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}


def scrape_zara():
    logger.info("Inside scrape_zara function...")
    # Send an HTTP GET request to Zara's website
    response = requests.get(
        'https://www.zara.com/in/en/category/2299309/products',
        headers=headers)

    # Parse the response as JSON
    data = response.json()

    return data
