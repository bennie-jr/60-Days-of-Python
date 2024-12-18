import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
url = os.getenv("URL")

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
