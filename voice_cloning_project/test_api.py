import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")

if api_key:
    print("API key found successfully!")
    print("Key starts with:", api_key[:5])
else:
    print("API key NOT found!")