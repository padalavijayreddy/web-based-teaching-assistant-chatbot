import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Optionally, print the API key to verify it's loaded
print("API Key Loaded:", OPENAI_API_KEY)
