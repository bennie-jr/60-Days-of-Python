import requests
import selectorlib
from dotenv import load_dotenv
import smtplib, ssl
import os
import time
import sqlite3


load_dotenv(override=True)

URL = "http://programmer100.pythonanywhere.com/tours/"


class Event:
    def scrapper(self, url):
        """Scrape the source page from the URL"""
        # response = requests.get(url, headers=HEADERS)
        response = requests.get(url)
        source = response.text
        return source


    def extraction(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tours"]
        return value


class Email:
    def send(self, message):
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


class Database:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)


    def data_store(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO events VALUES(?, ?, ?)", row)
        self.connection.commit()


    def read_data(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        band, city, date = row
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM events Where band=? AND city=? AND date=?", (band, city, date))
        rows = cursor.fetchall()
        print(rows)
        return rows


if __name__ == "__main__":
    while True:
        event = Event()
        scrapped = event.scrapper(URL)
        extracted = event.extraction(scrapped)
        print(extracted)

        if extracted != "No upcoming tours":
            database = Database(db_path="data.db")
            row = database.read_data(extracted)
            if not row:
                database.data_store(extracted)
                email = Email()
                email.send(message='A new event was found.')
        time.sleep(2)
        
