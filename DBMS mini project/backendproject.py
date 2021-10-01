import mysql.connector
class miniproject():
    train_no=[]
    def connect(self):
        con=mysql.connector.connect(host="localhost",user="root",passwd="Bhadouria123",database="train_reservation")
        cur=con.cursor()
        cur.execute("")
        con.commit()
        con.close()

    def login(self,user,pwd):
        database=mysql.connector.connect(host="localhost",user="root",passwd="Bhadouria123",database="train_reservation")
        cur=database.cursor()  
        check=cur.execute(f"select username from account where username='{user}'")
        result=cur.fetchall()
        if result != []:
            check=cur.execute(f"select password from account where username='{user}'")
            result=cur.fetchall()
            if pwd == result[0][0]:
                return 1
            else:
                return 2
        else:
            return 0
    def signup(self,name,pwd,em,ci,phone):
        conn=mysql.connector.connect(host="localhost",user="root",passwd="Bhadouria123",database="train_reservation")
        cur=conn.cursor()
        insert=cur.execute(f"insert into `Account` values ('{name}','{pwd}','{em}','{ci}');")
        insert=cur.execute(f"insert into `Contact` values ('{name}','{phone}');")
        conn.commit()
        conn.close()
    def gettraindetails(self,fro,to,day):
        database=mysql.connector.connect(host="localhost",user="root",passwd="Bhadouria123",database="train_reservation")
        cur=database.cursor() 
        train=cur.execute(f"""select arrival.train_no,train.name,departure.station_code,departure.departure_time,arrival.station_code,arrival.arrival_time
                                from arrival
                                inner join departure on arrival.train_no=departure.train_no
                                inner join train on train.train_no=departure.train_no
                                where departure.station_code='{fro}' and arrival.station_code='{to}' and train.rest!={day};""")
        result=cur.fetchall()
        print(result)
        train_no=[]
        count=0 
        if result != []:
            for a in result:
                count+=1
            for a in range(0,count):
                train_no.append(result[a][0])
        database.commit()
        database.close()
    
    def insertticket(self,tn,seats,uname,d):
        database=mysql.connector.connect(host="localhost",user="root",passwd="Bhadouria123",database="train_reservation")
        cur=database.cursor() 
        cur.execute(f"""insert into ticket(train_no,username,no_of_passengers,d_of_journey) values({tn},'{uname}',{seats},'{d}');
                    """)
        database.commit()
        database.close()

    def PassengerDetails(self,det):
        database=mysql.connector.connect(host="localhost",user="root",passwd="Bhadouria123",database="train_reservation")
        cur=database.cursor() 
        cur.execute(f"""insert into Passenger(first_name,last_name,gender,phone_no,ticket_no,age,class) values 
                        ('{det[1]}','{det[2]}','{det[0]}','{det[4]}',{det[5]},'{det[3]}','{det[6]}');
                    """)
        database.commit()
        database.close()

        


