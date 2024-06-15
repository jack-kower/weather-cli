import requests
from dotenv import load_dotenv
import os

# Loads contents of .env file into the script's environment
load_dotenv()

# Give the API key access to the script

API_KEY = os.getenv('API_KEY')

# check to see if this is the same as the API key in the .env file
print(API_KEY)
