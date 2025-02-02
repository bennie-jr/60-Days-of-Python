import requests
import selectorlib
import time
import sqlite3


connection = sqlite3.connect("temp-date.db")
now = time.strftime("%y-%m-%d-%H-%M-%S")

URL = "http://programmer100.pythonanywhere.com/"


def scrapper(url):
    response = requests.get(url)
    source = response.text
    return source


def extraction(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)['tours']
    return value


def data_store(extracted):
    row = extracted
    date = now
    print(date)
    print(row)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperature VALUES(?, ?)", (date, row))
    connection.commit()




if __name__ == "__main__":
    scrapped = scrapper(URL)
    extracted = extraction(scrapped)
    
    data_store(extracted)