


# Ethiopian Medical Business Data Warehouse

## Overview
This project involves building a data warehouse to store data on Ethiopian medical businesses scraped from Telegram channels. It also includes developing a data scraping and cleaning pipeline, applying object detection using YOLO on collected images, and exposing the collected data via a FastAPI-based API.

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
- [Task 3: Object Detection Using YOLO](#task-3-object-detection-using-yolo)
  - [YOLO Setup](#yolo-setup)
  - [Running Object Detection](#running-object-detection)
- [Task 4: API Exposure with FastAPI](#task-4-api-exposure-with-fastapi)
  - [API Endpoints](#api-endpoints)
- [Logging and Monitoring](#logging-and-monitoring)

---

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
Data is scraped from public Telegram channels related to Ethiopian medical businesses.

#### Steps:
1. **Install Telethon for Telegram Scraping:**
   ```bash
   pip install telethon
   ```

2. **Running the Telegram Scraper:**
   The `telegram_scraper.py` script extracts messages, media, and links from specific Telegram channels:
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
   All raw data scraped from the channels is stored in the `data/raw/` directory in CSV or JSON format.

### Image Scraping
Images are scraped from specific Telegram channels to be used for object detection.

#### Steps:
1. **Running the Image Scraper:**
   The `image_scraper.py` script collects images from Telegram channels like Chemed and Lobelia Cosmetics:
   ```bash
   python scripts/image_scraper.py
   ```

2. **Store Images:**
   Scraped images are stored in the `data/images/` directory for further processing.

## Task 2: Data Cleaning and Transformation

### Data Cleaning
Once raw data is collected, it needs to be cleaned for consistency and usability.

#### Cleaning Steps:
1. **Removing Duplicates:** Duplicate entries are removed.
2. **Handling Missing Values:** Missing values are filled or removed.
3. **Standardizing Formats:** Standardize formats for text, dates, and numbers.
4. **Data Validation:** Validate data formats for consistency.

#### Run the Data Cleaning Script:
```bash
python scripts/data_cleaning.py
```

### DBT for Data Transformation

**DBT (Data Build Tool)** transforms the cleaned data to prepare it for storage in the data warehouse.

#### Steps:
1. **Set Up DBT:**
   ```bash
   dbt init dbt_project
   ```

2. **Define Models:** SQL models are added to the `dbt_project/models/` folder.
3. **Run DBT Models:**
   ```bash
   dbt run
   ```

4. **Testing and Documentation:**
   ```bash
   dbt test
   dbt docs generate
   dbt docs serve
   ```

---

## Task 3: Object Detection Using YOLO

### YOLO Setup

Object detection is performed using the YOLO (You Only Look Once) model on images scraped from Telegram channels.

#### Steps:

1. **Install YOLOv5:**
   Clone the YOLOv5 repository and install dependencies:
   ```bash
   git clone https://github.com/ultralytics/yolov5.git
   cd yolov5
   pip install -r requirements.txt
   ```

2. **Prepare Image Data:**
   Ensure that all images scraped in Task 1 are stored in the `data/images/` directory.

3. **Configure YOLOv5 Model:**
   Download a pre-trained YOLOv5 model or train your own model using custom data. Store the model weights in the `weights/` directory.

4. **Run Object Detection:**
   Run the object detection script on the scraped images:
   ```bash
   python detect.py --source ../data/images --weights weights/yolov5s.pt --conf 0.4 --save-txt
   ```

5. **Store Detection Results:**
   Object detection results (bounding boxes, class labels, confidence scores) are saved in the `data/detections/` directory.

### Running Object Detection

To run YOLO object detection on scraped images, use the following script:
```bash
python scripts/run_yolo.py
```

---

## Task 4: API Exposure with FastAPI

### API Overview

The FastAPI application exposes endpoints to interact with the cleaned and processed data.

### API Endpoints

- **GET /data**: Retrieve all data from the warehouse.
- **GET /data/{id}**: Retrieve data by specific ID.
- **POST /data**: Insert new data entry into the warehouse.
- **PUT /data/{id}**: Update an existing data entry.
- **DELETE /data/{id}**: Delete a data entry.

### Run FastAPI Server

1. **Install FastAPI and Uvicorn:**
   ```bash
   pip install fastapi uvicorn
   ```

2. **Run the FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`.

---

## Logging and Monitoring

- **Logging:** Scraping, cleaning, object detection, and API scripts include logging functionality to track progress and identify errors. Logs are stored in the `logs/` directory.
  
- **Monitoring:** Use logs to monitor the performance and troubleshoot errors.

