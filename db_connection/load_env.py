import os
from dotenv import load_dotenv
import streamlit as st

def load_env():
   
    if os.getenv('STREAMLIT_ENV') == 'production':
        # For production, ensure that the necessary secrets are available in st.secrets
        required_secrets = ["DB_NAME", "DB_HOST", "DB_USER", "DB_PASSWORD", "DB_PORT"]
        for secret in required_secrets:
            if secret not in st.secrets:
                raise EnvironmentError(f"Missing {secret} in Streamlit secrets.")
        print("Environment variables loaded from Streamlit secrets (production).")
    else:
        # Load from .env file for local development
        env_file = os.path.join(os.getcwd(), '.env')
        if os.path.exists(env_file):
            load_dotenv(env_file)
            print("Environment variables loaded successfully from .env file (local development).")
        else:
            raise FileNotFoundError(f"The .env file could not be found at {env_file}.")
