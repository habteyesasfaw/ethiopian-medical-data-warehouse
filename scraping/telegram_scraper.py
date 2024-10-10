import csv
import os
import asyncio
from telethon import TelegramClient
from dotenv import load_dotenv
from logging import getLogger
# Load environment variables
load_dotenv('.env')
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
phone = os.getenv('TG_PHONE')

# Initialize logger
logger = getLogger('Telegram_Scraper')

# Function to scrape data from a single channel
async def scrape_channel(client, channel_username, writer, media_dir):
    try:
        entity = await client.get_entity(channel_username)
        channel_title = entity.title  # Extract the channel's title
        logger.info(f"Scraping started for {channel_title} ({channel_username})")
        
        async for message in client.iter_messages(entity, limit=10000):
            media_path = None
            if message.media and hasattr(message.media, 'photo'):
                # Create a unique filename for the photo
                filename = f"{channel_username}_{message.id}.jpg"
                media_path = os.path.join(media_dir, filename)
                # Download the media to the specified directory if it's a photo
                await client.download_media(message.media, media_path)
                logger.info(f"Downloaded media from message ID {message.id} in {channel_username}")
            
            # Write the channel title along with other data
            writer.writerow([channel_title, channel_username, message.id, message.message, message.date, media_path])
        
        logger.info(f"Scraping completed for {channel_title} ({channel_username})")
    
    except Exception as e:
        logger.error(f"Error scraping {channel_username}: {e}")

# Main function to run the scraper
async def main():
    client = TelegramClient('scraping_session', api_id, api_hash)
    
    await client.start()
    logger.info("Telegram client started successfully.")

    # Create a directory for media files
    media_dir = 'photos'
    os.makedirs(media_dir, exist_ok=True)
    logger.info(f"Media directory set at {media_dir}")

    # Open the CSV file and prepare the writer
    with open('telegram_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Channel Title', 'Channel Username', 'ID', 'Message', 'Date', 'Media Path'])  # Include channel title in the header

        # List of channels to scrape
        channels = [
            'DoctorsET',
            'CheMed123',
            'lobelia4cosmetics',
            'yetenaweg',
            'EAHCI'
        ]

        # Iterate over channels and scrape data into the single CSV file
        for channel in channels:
            logger.info(f"Starting scrape for channel {channel}")
            await scrape_channel(client, channel, writer, media_dir)
            logger.info(f"Finished scrape for channel {channel}")

    await client.disconnect()
    logger.info("Telegram client disconnected.")

# Run the scraper
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.error(f"Failed to run scraper: {e}")
