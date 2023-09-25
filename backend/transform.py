import pandas as pd
import re
from backend.utils import log_config

# Set up logging
log_config.setup_logging()

# Create a logger for transform.py
logger = log_config.get_logger(__name__)


def zara_transform(data):
    logger.info("Inside zara_transform() function...")
    all_data = []

    # Iterate through product groups and their elements
    for group in data["productGroups"]:
        for element in group["elements"]:
            try:
                for component in element["commercialComponents"]:
                    name = component["name"]
                    price = component['price'] / 100
                    old_price = component['oldPrice'] / 100
                    discount_percent = component['displayDiscountPercentage']
                    family = component['familyName']

                    for xmedia in component['detail']['colors']:
                        color = xmedia['name']
                        for image in xmedia['xmedia']:
                            img_url = f"https://static.zara.net/photos//{image['path']}/w/1024/{image['name']}.jpg?ts={image['timestamp']}"
                            np = (name, price, old_price, discount_percent, color, family, img_url)
                    all_data.append(np)
            except KeyError:
                pass

    logger.info("Creating the zara_onsale_df...")
    # Create a DataFrame with the extracted data
    zara_onsale_df = pd.DataFrame(all_data,
                                  columns=['product_name', 'price', 'og_price', 'discount_percent', 'product_color',
                                           'family', 'img_url'])

    logger.info("Changing data types of price and og_price columns..")
    zara_onsale_df['price'] = zara_onsale_df['price'].astype('float64')
    zara_onsale_df['og_price'] = zara_onsale_df['og_price'].astype('float64')

    logger.info("Successfully executed zara_transform() function!!")
    return zara_onsale_df


def uniqlo_transform(data):
    logger.info("Inside uniqlo_transform() function...")
    uniqlo_products = []

    for products in data:
        for item in products:
            name = item['name']
            price = item['prices']['promo']['value']
            old_price = item['prices']['base']['value']
            product_id = item['productId']
            product_link = f"https://www.uniqlo.com/in/en/products/{product_id}"
            img_url = item['images']['main'][0]['url']

            product_data = (product_id, name, price, old_price, product_link, img_url)
            uniqlo_products.append(product_data)

    logger.info("Creating uniqlo_onsale_df...")
    uniqlo_onsale_df = pd.DataFrame(uniqlo_products,
                                    columns=['product_id', 'product_name', 'price', 'og_price', 'product_link',
                                             'img_url'])


    logger.info("Changing uniqlo_df columns data types..")
    uniqlo_onsale_df['price'] = uniqlo_onsale_df['price'].astype('float64')
    uniqlo_onsale_df['og_price'] = uniqlo_onsale_df['og_price'].astype('float64')

    logger.info("Successfully executed uniqlo_transform() function!!")
    return uniqlo_onsale_df


def hm_transform(data):
    logger.info("Inside hm_transform() function...")
    all_products = []

    for product in data['products']:
        name = product['title']
        price = product['redPrice']
        og_price = product['price']
        product_link = f"https://www2.hm.com{product['link']}"

        for image in product['image']:
            img_url = image['src']

        hm_data = (name, price, og_price, product_link, img_url)
        all_products.append(hm_data)

    logger.info("Creating the hm_onsale_df...")
    hm_onsale_df = pd.DataFrame(all_products, columns=['product_name', 'price', 'og_price', 'product_link', 'img_url'])

    hm_onsale_df['price'] = hm_onsale_df['price'].str.replace("Rs.", "").str.replace(",", "").astype('float64')
    hm_onsale_df['og_price'] = hm_onsale_df['og_price'].str.replace("Rs.", "").str.replace(",", "").astype('float64')
    hm_onsale_df['img_url'] = "https:" + hm_onsale_df['img_url']
    hm_onsale_df['img_url'] = hm_onsale_df['img_url'].apply(lambda x: re.sub(r'"', '', x))

    logger.info("Successfully executed hm_transform() function!!")
    return hm_onsale_df
