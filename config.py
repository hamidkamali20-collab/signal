import os
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

# Securely load the API Key
API_KEY = os.getenv("API_KEY", "YOUR_API_KEY_HERE")
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.example.com/v1")
