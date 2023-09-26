# Fashion Sale Explorer

## Table of Contents

- [About](#about)
- [Key Features](#key-features)
- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [How To Use](#how-to-use)

## About

Fashion Sale Explorer is a Python-based web application that scrapes, transforms, and displays fashion sale data from top fashion brands like Zara, H&M and Uniqlo. The app allows users to explore the latest fashion sales and discounts from these brands and provides an easy-to-use interface to find the best deals.

## Key Features

- **Real-Time Sales Tracking:** Stay updated on the latest sales from your favorite fashion brands.
- **Brand-Specific Scrapers:** Custom web scrapers for each brand ensure accurate and up-to-date product data.
- **Logging Mechanism:** Streamlined debugging with a robust error-handling mechanism.
- **User-Friendly UI:** Seamlessly integrated with Streamlit for an intuitive user experience.

## Project Overview

The project follows a structured workflow:

1. **Data Scraping**: Data is scraped from Zara, H&M and Uniqlo websites and saved in JSON format in the `data/raw` folder.

2. **Data Transformation**: Data is then transformed by selecting only the required data fields and changing the data types. The transformed data is saved in CSV format in the `data/processed` folder.

3. **Frontend**: `Streamlit` library is used for the frontend. The frontend displays the products in user-friendly manner.

## Project Structure
``` 
- sale_explorer/ 
	- backend/
		- data/
			- raw/
			- processed/
		- scrapers/
			- hm_scraper.py
			- zara_scraper.py
			- uniqlo_scraper.py
		- utils/
			- log_config.py
		- webdriver/
			- msedgedriver.exe
		- __init__.py
		- database.py
		- transform.py
	- frontend/
		- app.py
		- __init__.py
	- .gitignore
	- backend.log
	- main.py
	- requirements.txt
	- README.md 
```

## Technologies Used

- Python
- Pandas
- Requests
- Selenium
- BeautifulSoup4
- Streamlit

## How To Use

1. Clone this repository to your local machine.
  ```bash
  git clone git@github.com:ajitchincholkar/Fashion-Sale-Explorer.git
  ```

2. Install the required dependencies.
  ```bash
  pip install -r requirements.txt
  ```

3. Run the main.py. It runs the scrapers, the transform scripts and finally saves the products data in `data/raw` and `data/processed` folders.
  ```bash
  python main.py
  ```

4. Run the app.py to launch the web app.
  ```bash
  streamlit run frontend/app.py
  ```