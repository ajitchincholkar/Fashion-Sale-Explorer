from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from time import sleep
import json
from backend.utils import log_config

# Set up logging
log_config.setup_logging()

# Create a logger for uniqlo_scraper.py
logger = log_config.get_logger(__name__)


def scrape_hm():
    logger.info("Inside scrape_hm() function...")
    # Set a User-Agent string for Microsoft Edge on Windows
    webdriver_path = 'backend/webdriver/msedgedriver.exe'
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edg/92.0.902.78 Safari/537.36"

    options = webdriver.EdgeOptions()
    options.add_argument('--headless')
    options.add_argument(f'--user-agent={user_agent}')

    logger.info("Starting the webdriver...")
    # Create an instance of the Edge WebDriver
    service = Service(executable_path=webdriver_path)
    driver = webdriver.Edge(service=service, options=options)

    website = 'https://www2.hm.com/en_in/sale/men/view-all/_jcr_content/main/productlisting_9436.display.json?sort=stock&image-size=small&image=model&offset=0&page-size=500'
    driver.get(website)
    sleep(5)

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'html.parser')

    product_data = soup.find('div', hidden="true")
    product_json = product_data.text

    parsed_json = json.loads(product_json)

    driver.close()
    driver.quit()
    logger.info("Closed the driver!!")

    return parsed_json
