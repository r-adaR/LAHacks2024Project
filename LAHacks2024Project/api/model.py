import google.generativeai as genai
import os
from dotenv import load_dotenv

# Get the secret API key for Gemini
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Configure the app to use the API key
genai.configure(api_key=GOOGLE_API_KEY)

# Create the model using the latest Gemini version
model = genai.GenerativeModel('gemini-1.5-pro-latest')
