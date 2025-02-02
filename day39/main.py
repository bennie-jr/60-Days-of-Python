import requests
import selectorlib
from dotenv import load_dotenv
import smtplib, ssl
import os
import time
import sqlite3


load_dotenv(override=True)

URL = "http://programmer100.pythonanywhere.com/tours/"
# HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

connection = sqlite3.connect('data.db')

def scrapper(url):
    """Scrape the source page from the URL"""
    # response = requests.get(url, headers=HEADERS)
    response = requests.get(url)
    source = response.text
    return source


def extraction(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    receiver = "bensowahjr@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

    print("Email was sent!")


def data_store(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?, ?, ?)", row)
    connection.commit()


def read_data(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events Where band=? AND city=? AND date=?", (band, city, date))
    rows = cursor.fetchall()
    print(rows)
    return rows


if __name__ == "__main__":
    while True:
        scrapped = scrapper(URL)
        extracted = extraction(scrapped)
        print(extracted)

        if extracted != "No upcoming tours":
            row = read_data(extracted)
            if not row:
                data_store(extracted)
                send_email(message='A new event was found.')
        time.sleep(2)
        
