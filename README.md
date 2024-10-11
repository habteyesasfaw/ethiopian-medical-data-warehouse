

---

# Ethiopian Medical Business Data Warehouse

## Overview
This project involves building a data warehouse to store data on Ethiopian medical businesses scraped from Telegram channels. It also includes developing a data scraping and cleaning pipeline, which allows the transformation of raw data into a structured format for further analysis.

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Task 1: Data Scraping and Collection Pipeline](#task-1-data-scraping-and-collection-pipeline)
  - [Telegram Scraping](#telegram-scraping)
  - [Image Scraping](#image-scraping)
- [Task 2: Data Cleaning and Transformation](#task-2-data-cleaning-and-transformation)
  - [Data Cleaning](#data-cleaning)
  - [DBT for Data Transformation](#dbt-for-data-transformation)
- [Logging and Monitoring](#logging-and-monitoring)


```

## Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd my_project
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install DBT (Data Build Tool)**
   DBT is used for data transformation tasks:
   ```bash
   pip install dbt
   ```

## Task 1: Data Scraping and Collection Pipeline

### Telegram Scraping

In this task, data is scraped from public Telegram channels related to Ethiopian medical businesses.

#### Steps:
1. **Install Telethon for Telegram Scraping:**
   ```bash
   pip install telethon
   ```

2. **Running the Telegram Scraper:**
   The `telegram_scraper.py` script extracts messages, media, and links from specific Telegram channels.
   - Channels being scraped:
     - [DoctorsET](https://t.me/DoctorsET)
     - [Chemed Telegram Channel](https://t.me/lobelia4cosmetics)
     - [Yetenaweg](https://t.me/yetenaweg)
     - [EAHCI](https://t.me/EAHCI)
   - To run the scraper:
     ```bash
     python scripts/telegram_scraper.py
     ```

3. **Store Raw Data:**
   - All raw data scraped from the channels is stored in the `data/raw/` directory for further processing.
   - Data is stored in CSV format or as JSON files.

### Image Scraping

In this task, images are scraped from specific Telegram channels to be used for object detection in Task 3.

#### Steps:
1. **Running the Image Scraper:**
   - The `image_scraper.py` script collects images from channels such as Chemed and Lobelia Cosmetics.
   - To run the image scraper:
     ```bash
     python scripts/image_scraper.py
     ```
2. **Store Images:**
   - All scraped images are stored in the `data/images/` directory.
   - The file paths are stored in a temporary database or local CSV files for later processing.

## Task 2: Data Cleaning and Transformation

### Data Cleaning
Once the raw data is collected, it's important to clean it for consistency and usability.

#### Cleaning Steps:
1. **Removing Duplicates:**
   - Duplicate records and entries are removed to maintain data integrity.

2. **Handling Missing Values:**
   - Missing values are either filled using appropriate methods or removed depending on their relevance.

3. **Standardizing Formats:**
   - Formats for text, dates, and numeric values are standardized for consistency.

4. **Data Validation:**
   - Data is validated to ensure it's in a usable format for further analysis.

#### Run the Data Cleaning Script:
   ```bash
   python scripts/data_cleaning.py
   ```

### DBT for Data Transformation

**DBT (Data Build Tool)** is used to transform the cleaned data and prepare it for analysis and storage in the data warehouse.

#### Steps:
1. **Setting Up DBT:**
   ```bash
   dbt init dbt_project
   ```

2. **Define Transformation Models:**
   - SQL models in DBT define the transformation logic.
   - Add your models in the `dbt_project/models/` folder.

3. **Run DBT Models:**
   ```bash
   dbt run
   ```

4. **Testing and Documentation:**
   - Ensure data quality and generate documentation using DBT.
   ```bash
   dbt test
   dbt docs generate
   dbt docs serve
   ```

## Logging and Monitoring

- **Logging:** The scraping, cleaning, and transformation scripts include logging functionality to track the progress and identify issues.
  - Logs are stored in the `logs/` directory.

- **Monitoring:** Use logs to monitor performance and troubleshoot errors.


