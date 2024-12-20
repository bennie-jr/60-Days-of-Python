import requests
from dotenv import load_dotenv
import os
from send_emails import send_email

load_dotenv()

api_key = os.getenv("API_KEY")
url = os.getenv("URL")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles, descriptions and links
body = ""
for article in content["articles"][:20]:
    body = "Subject: Today's Newsletter" + "\n" + body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")


send_email(body)