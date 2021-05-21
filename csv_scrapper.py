import requests
from bs4 import BeautifulSoup
import random
from csv import DictWriter
from time import sleep

def scraping_quotes():
    url="http://quotes.toscrape.com"
    nextbtn="/page/1"
    qoutes=[]
    while nextbtn:
        request=requests.get(f"{url}{nextbtn}")
        print(f"now getting data from {url}{nextbtn}.......")
        data=request.text
        soup=BeautifulSoup(data,"html.parser")
        link=soup.find(class_="next")
        nextbtn=link.find("a")["href"] if link else None
        for q in soup.findAll(class_="quote"):
            qoutes.append({
                "quote":q.find(class_="text").get_text(),
                "author":q.find(class_="author").get_text(),
                "bio":q.find("a")["href"]
        })
        sleep(2)
    return qoutes


def making_csvfile(qu):
    with open("quote_data.csv","w") as file:
        headings=["quote","author","bio"]
        csv_writer=DictWriter(file, fieldnames=headings)
        csv_writer.writeheader()
        for each in qu:
            csv_writer.writerow(each)

q=scraping_quotes()
making_csvfile(q)