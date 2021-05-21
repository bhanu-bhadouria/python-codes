import termcolor
import pyfiglet
import requests
import random

print(termcolor.colored(pyfiglet.figlet_format("DAD JOKE3000"),color="blue"))
c='y'
while c=='y':
    def getjoke(topic):
        url="https://icanhazdadjoke.com/search"
        response=requests.get(url,headers={"Accept":"application/json"},
        params={"term":topic,"limit":1})
        data=response.json()
        count=data["total_jokes"]
        if count==1:
            print("found 1 joke:")
            print(data["results"][0]["joke"])
        elif count > 1:
            print(f"found {count} jokes")
            print(random.choice(data["results"])["joke"])
        else:
            print("sry no joke found")

    t=input("pls enter the topic you want to find out: ")
    getjoke(t)
    c=input("do you wish to continue(y/n): ")
