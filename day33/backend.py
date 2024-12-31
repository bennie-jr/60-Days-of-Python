from dotenv import load_dotenv
import os
import requests

load_dotenv(override=True)

api_key = os.getenv("API_KEY")

def get_data(place, days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    get_data(place="Tokyo")