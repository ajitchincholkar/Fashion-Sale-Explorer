# Fashion Sale Explorer

## Table of Contents

- [About](#about)
- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Data Scraping](#data-scraping)
  - [Data Transformation](#data-transformation)
  - [Frontend](#frontend)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## About

Fashion Sale Explorer is a Python-based web application that scrapes, transforms, and displays fashion sale data from Zara and Uniqlo. The app allows users to explore the latest fashion sales and discounts from these brands and provides an easy-to-use interface to find the best deals.

## Project Overview

The project follows a structured workflow:

1. **Data Scraping**: Data is scraped from Zara and Uniqlo websites and saved in JSON format in the `data/raw` folder.

2. **Data Transformation**: The `transform` function processes the scraped data and saves it in CSV format in the `data/processed` folder. Additionally, the transformed data is loaded into a PostgreSQL database.

3. **Frontend**: The web-based frontend fetches data from the PostgreSQL database, allowing users to select a brand and view the available products on sale.
