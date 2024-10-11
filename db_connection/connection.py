import pandas as pd
import psycopg2
import os

class PostgresConnection:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None

    def connect(self):
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
            print(f"Error connecting to database: {e}")

    def insert_dataframe(self, df, table_name):
        """Insert DataFrame data into PostgreSQL table, handling duplicates."""
        try:
            if self.conn:
                cursor = self.conn.cursor()
                
                # Drop duplicates based on the 'ID' column
                df = df.drop_duplicates(subset=['ID'], keep='first')
            

                # Create an insert query template with the correct column names
                insert_query = f"""
                INSERT INTO {table_name} ("Channel Title", "Channel Username", "ID", "Message", "Date", "Media Path")
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT ("ID") DO NOTHING;  -- Ignore duplicates based on ID
                """
                
                # Iterate over DataFrame rows and insert into the database
                for index, row in df.iterrows():
                    try:
                        cursor.execute(insert_query, (
                            row['Channel Title'],
                            row['Channel Username'],
                            row['ID'],
                            row['Message'],
                            row['Date'],
                            row['Media Path']
                        ))
                    except Exception as insert_error:
                        print(f"Error inserting row {index}: {insert_error}")
                        self.conn.rollback()  # Rollback on error for this row
            
                self.conn.commit()
                print(f"{len(df)} records inserted into {table_name} table.")
                cursor.close()
            else:
                print("No connection found.")
        except Exception as e:
            print(f"Error inserting data: {e}")

    def close(self):
        if self.conn:
            self.conn.close()
            print("Connection closed.")

# Example usage
if __name__ == "__main__":
    # Database connection parameters
    dbname = "EthMedHub"
    user = "postgres"
    password = "root"
    host = "localhost"
    port = "5432"

    # Create an instance of the PostgresConnection
    db_connection = PostgresConnection(dbname, user, password, host, port)
    db_connection.connect()

    # Load your CSV data into a DataFrame
    df = pd.read_csv('path/to/your/data.csv', sep='\t')  # Adjust the path to your CSV file and set sep='\t' if it's tab-separated

    # Insert the DataFrame into the PostgreSQL table
    db_connection.insert_dataframe(df, 'medical_data')

    # Close the database connection
    db_connection.close()
