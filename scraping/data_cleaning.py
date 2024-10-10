import pandas as pd
import os
import logging

# Set up logging
logging.basicConfig(
    filename="../scraping/logging/data_cleaning.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Function to clean the scraped data
def clean_data(input_file, output_file):
    try:
        # Load raw data
        logging.info(f"Loading raw data from {input_file}")
        data = pd.read_csv(input_file)
        
        # Remove duplicate
        logging.info("Removing duplicates")
        data.drop_duplicates(inplace=True)
        
        # Handle missing values (example: filling missing values)
        logging.info("Handling missing values")
        data.fillna("Unknown", inplace=True)
        
        # Standardize formats (example: standardizing date formats)
        if 'date' in data.columns:
            logging.info("Standardizing date format")
            data['date'] = pd.to_datetime(data['date'], errors='coerce')
        
        # Data validation (example: validating certain columns)
        if 'name' in data.columns and 'contact' in data.columns:
            logging.info("Validating data")
            valid_data = data[data['name'].notnull() & data['contact'].notnull()]
        else:
            valid_data = data
        
        # Save cleaned data
        logging.info(f"Storing cleaned data to {output_file}")
        valid_data.to_csv(output_file, index=False)
        logging.info("Data cleaning completed successfully")

    except Exception as e:
        logging.error(f"Error during data cleaning: {str(e)}")
        raise

if __name__ == "__main__":
    raw_data_file = "../data/telegram_data.csv"
    cleaned_data_file = "../data/cleaned_telegram_data.csv"
    
    clean_data(raw_data_file, cleaned_data_file)
