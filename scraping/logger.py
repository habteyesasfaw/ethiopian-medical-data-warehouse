import logging
from telethon import TelegramClient
import csv
import os
from dotenv import load_dotenv

def get_logger(name):
    # Ensure the logs directory exists
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    ## Get the logger instance
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent adding duplicate handlers if logger is called multiple times
    if not logger.hasHandlers():
        try:
            # File handler for logging to file
            file_handler = logging.FileHandler(os.path.join(log_dir, 'eda_log.log'))
            file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)

            # Console handler for logging to console
            console_handler = logging.StreamHandler()
            console_formatter = logging.Formatter('%(levelname)s - %(message)s')
            console_handler.setFormatter(console_formatter)
            logger.addHandler(console_handler)

            logger.info("Logger initialized successfully.")
        except Exception as e:
            print(f"Failed to create log file: {e}")
            logger.error(f"Failed to create log file: {e}")
    else:
        logger.info("Logger already initialized.")

    return logger

# Example usage
logger = get_logger('EDA_Logger')
logger.info("Starting the exploratory data analysis...")
