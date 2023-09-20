from backend.scrapers.zara_scraper import scrape_zara
from backend.scrapers.uniqlo_scraper import scrape_uniqlo
from backend.database import create_connection
from backend.transform import zara_transform, uniqlo_transform
from backend.utils import log_config
import json

# Set up logging
log_config.setup_logging()

# Create a logger for main.py
logger = log_config.get_logger(__name__)


def main():
    logger.info("STARTED THE SCRAPING...")
    zara_json = scrape_zara()
    uniqlo_json = scrape_uniqlo()
    logger.info("SCRAPING DONE!!")

    with open('backend/data/raw/zara_raw.json', 'w') as json_file:
        json.dump(zara_json, json_file, indent=1)
    with open('backend/data/raw/uniqlo_raw.json', 'w') as json_file:
        json.dump(uniqlo_json, json_file, indent=1)
    logger.info("SAVED SCRAPED DATA TO raw FOLDER")

    logger.info("TRANSFORMING THE DATA...")
    zara_df = zara_transform(zara_json)
    uniqlo_df = uniqlo_transform(uniqlo_json)
    logger.info("TRANSFORMATION DONE!!")

    zara_df.to_csv('backend/data/processed/zara_onsale.csv', index=False)
    uniqlo_df.to_csv('backend/data/processed/uniqlo_onsale.csv', index=False)
    logger.info("SAVED THE TRANSFORMED DATA TO processed FOLDER")

    logger.info("CONNECTING TO THE POSTGRES DB...")
    engine = create_connection('onsale_db')

    logger.info("WRITING THE TRANSFORMED DATA TO THE POSTGRES DB...")
    zara_df.to_sql(name='zara_sale', con=engine, if_exists='replace', index=False)
    uniqlo_df.to_sql(name='uniqlo_sale', con=engine, if_exists='replace', index=False)
    logger.info("SUCCESSFULLY SAVED DATA TO THE DB!!!")


if __name__ == '__main__':
    main()
    logger.info("ALL DONE!!!")
