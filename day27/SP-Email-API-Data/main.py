import requests
from dotenv import load_dotenv
import os
from send_emails import send_email

load_dotenv()

api_key = os.getenv("API_KEY")
url = os.getenv("URL")

user_email = "bensowahjr@gmail.com"
request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
    body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")


send_email(body)
