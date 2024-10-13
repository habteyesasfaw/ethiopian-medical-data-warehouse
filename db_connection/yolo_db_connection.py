import pandas as pd
import psycopg2
import logging

class PostgresConnection:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user  # Corrected this line
        self.password = password
        self.host = host
        self.port = port
        self.conn = None

    def connect(self):
        """Connect to the PostgreSQL database."""
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Connected to PostgreSQL Database!")
        except Exception as e:
            logging.error(f"Error connecting to database: {e}")

    def create_table(self, table_name):
        """Create a table for YOLO detection results if it doesn't exist."""
        try:
            if self.conn:
                cursor = self.conn.cursor()
                cursor.execute(f"""
                    CREATE TABLE IF NOT EXISTS {table_name} (
                        id SERIAL PRIMARY KEY,
                        image TEXT,
                        class_label TEXT,
                        confidence REAL,
                        xmin REAL,
                        ymin REAL,
                        xmax REAL,
                        ymax REAL
                    )
                """)
                self.conn.commit()
                cursor.close()
                print(f"Table {table_name} is ready.")
        except Exception as e:
            logging.error(f"Error creating table: {e}")

    def insert_dataframe(self, df, table_name):
        """Insert YOLO detection data into PostgreSQL table."""
        if self.conn:
            cursor = self.conn.cursor()

            # Drop duplicates based on the 'id' column
            df = df.drop_duplicates(subset=['id'], keep='first')

            # Create an insert query template
            insert_query = f"""
            INSERT INTO {table_name} (image, class_label, confidence, xmin, ymin, xmax, ymax)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING;  -- Ignore duplicates based on id
            """
            
            try:
                for index, row in df.iterrows():
                    cursor.execute(insert_query, (
                        row['image'],
                        row['class_label'],
                        row['confidence'],
                        row['xmin'],
                        row['ymin'],
                        row['xmax'],
                        row['ymax']
                    ))
                self.conn.commit()
                print(f"{len(df)} records inserted into {table_name} table.")
            except Exception as insert_error:
                logging.error(f"Error inserting rows: {insert_error}")
                self.conn.rollback()  # Rollback on error
            finally:
                cursor.close()
        else:
            print("No connection found.")

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            print("Connection closed.")

# Configuration dictionary for database connection
db_config = {
    'dbname': "EthMedHub",
    'user': "postgres",
    'password': "root",
    'host': "localhost",
    'port': "5432"
}

# Example usage
if __name__ == "__main__":
    # Create an instance of the PostgresConnection using db_config
    pg_conn = PostgresConnection(**db_config)
    
    # Connect to the PostgreSQL database
    pg_conn.connect()
    
    # Create the table if it does not exist
    pg_conn.create_table('yolo_detections')

    # Example DataFrame for YOLO detection results
    data = {
        'image': ['image1.jpg', 'image2.jpg'],
        'class_label': ['person', 'car'],
        'confidence': [0.98, 0.85],
        'xmin': [100, 120],
        'ymin': [150, 180],
        'xmax': [200, 250],
        'ymax': [300, 350]
    }

    df = pd.DataFrame(data)

    # Insert the DataFrame into the PostgreSQL table
    pg_conn.insert_dataframe(df, 'yolo_detections')

    # Close the database connection
    pg_conn.close()
