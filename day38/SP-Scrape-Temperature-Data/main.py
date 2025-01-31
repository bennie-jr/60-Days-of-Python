import requests
import selectorlib
import time


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
    with open("data.txt", 'a+') as file:
        file.write(now +','+ extracted + "\n")




if __name__ == "__main__":
    scrapped = scrapper(URL)
    extracted = extraction(scrapped)
    
    data_store(extracted)