import requests
from bs4 import BeautifulSoup
from csv import writer
#https://www.rithmschool.com/blog
response=requests.get("https://www.rithmschool.com/blog")
soup=BeautifulSoup(response.text,"html.parser")
articles=soup.findAll("article")
with open("article.csv","w") as file:
    csv_writer=writer(file)
    csv_writer.writerow(["title","link","date_time"])
    for article in articles:
        a_tag=article.find("a")
        title=a_tag.get_text()
        href=a_tag["href"]
        time=article.find("time")["datetime"]
        csv_writer.writerow([title,href,time])