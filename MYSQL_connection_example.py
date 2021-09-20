import mysql.connector

database=mysql.connector.connect(host="localhost",user="root",passwd="Bhadouria123",database="train_reservation")

cur=database.cursor()

cur.execute("select * from train ")

result=cur.fetchall()

print(result)
