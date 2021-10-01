import mysql.connector

database=mysql.connector.connect(host="localhost",user="root",passwd="Bhadouria123",database="train_reservation")

cur=database.cursor()
name="admin"
cur.execute(f"select * from account where username='{name}';")

result=cur.fetchall()

print(result)
