import requests
import sqlite3
from bs4 import BeautifulSoup


def scrape(url):
    request=requests.get(url)
    data=request.text
    soup=BeautifulSoup(data,"html.parser")
    books=soup.find_all("article")
    all_books=[]
    for book in books:
        title=gettitle(book)
        price=float(getprice(book))
        rating=getrating(book)
        data_col=(title,price,rating)
        all_books.append(data_col)
    return all_books

def sql(all_books):
    con=sqlite3.connect("Book_db.db")
    c=con.cursor()
    c.execute("create table books(title text,price real,rating integer);")
    c.executemany("insert into books values (?,?,?)",all_books)
    con.commit()
    con.close()

def gettitle(book):
    title=book.find("h3").find("a")["title"]
    return title

def getprice(book):
    price=book.find(class_="price_color").get_text()
    return price.replace("Â£","")

def getrating(book):
    rating_i={"Zero":0,"One":1,"Two":2,"Three":3,"Four":4,"Five":5}
    para=book.select(".star-rating")[0]
    word_rating=para.get_attribute_list("class")[-1]
    return rating_i[word_rating]

book_data=scrape("https://books.toscrape.com/")
sql(book_data)
