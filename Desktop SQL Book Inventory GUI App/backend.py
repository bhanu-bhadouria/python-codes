import sqlite3

def conncet():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("create table if not exists book (id INTEGER primary key, title TEXT, author TEXT,year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    tuple1=(title,author,year,isbn)
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("insert into book values(NULL,?,?,?,?)",tuple1)
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("select * from book")
    data=cur.fetchall()
    conn.commit()
    conn.close()
    return data

def search(title="",author="",year="",isbn=""):
    tuple1=(title,author,year,isbn)
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("select * from book where title=? or author=? or year=? or isbn=?",tuple1)
    data=cur.fetchall()
    conn.commit()
    conn.close()
    return data

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("delete from book where id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    tuple1= (title,author,year,isbn,id)
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("update book set title=?,author=?,year=?,isbn=? where id=?",tuple1)
    conn.commit()
    conn.close()


conncet()
