import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv(override=True)

api_key = os.getenv("API_KEY")
url = os.getenv("URL")

# Get request data as a dictionary
request = requests.get(url)
content = request.json()

st.title(content["title"])

# Easier method to get the image on the webpage
# st.image(content["url"])

# Get the image url data for download
image_url = content["url"]
image_request = requests.get(image_url)

# Download the image
with open("image.jpg", "wb") as file:
    file.write(image_request.content)

st.image("image.jpg")
st.write(content["explanation"])