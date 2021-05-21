import requests
from bs4 import BeautifulSoup
import random
from csv import DictReader

url="http://quotes.toscrape.com"

def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader=DictReader(file)
        return list(csv_reader)


def game(qoutes):
    ch="y"  
    while ch == "y":
        randomchoice=random.choice(qoutes)
        biolink=randomchoice["bio"]
        request=requests.get(f"{url}{biolink}")
        data=request.text
        soup=BeautifulSoup(data,"html.parser")
        guess_remaining=4
        print(randomchoice["quote"])
        print(randomchoice["author"])
        while guess_remaining > 0:
            guess=input(f"pls enter your guessed author, guess remaining {guess_remaining} : \n")
            guess_remaining-=1
            if guess.lower()==randomchoice["author"].lower():
                print("YOU GUESSED IT!!!")
                break
            if guess_remaining==3:
                borndate=soup.find(class_="author-born-date").get_text()
                bornplace=soup.find(class_="author-born-location").get_text()
                print(f"the author was born on {borndate} {bornplace}")
            elif guess_remaining==2:
                firstinitial=randomchoice["author"][0].upper()
                print(f"the author's first name starts with {firstinitial}")
            elif guess_remaining==1:
                name=randomchoice["author"].split(" ")
                lastinitial=name[1][0].upper()
                print(f"the author's last name starts with {lastinitial}")
            else:
                name=randomchoice["author"]
                print(f"sry you have ran out of options the answer is : {name}")
                break
        ch=input("do you wish to continue (y/n): ")

q=read_quotes("quote_data.csv")
game(q)

