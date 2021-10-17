import mysql.connector
import backendproject
import calendar
from datetime import datetime
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button

Builder.load_file("designproject.kv")

u=""
class LoginScreen(Screen):
    def login(self,uname,pword):
        status=0
        globals_list=globals()
        status=backendproject.miniproject.login(self,uname,pword)
        if status == 0:
            self.ids.login_wrong.text="username does not exist"
        elif status == 1:
            globals_list["u"]=uname
            self.ids.login_wrong.text="LOGIN SUCCESSFULL"
            self.manager.transition.direction = "left"
            self.manager.current = "TR_screen"
        else:
            self.ids.login_wrong.text="PASSWORD INCORRECT"
    def sign_up(self):
        self.manager.transition.direction = "left"
        self.manager.current = "Signup_screen"
class SignupScreen(Screen):
    def sign(self,n,p,e,c,ph):
        backendproject.miniproject.signup(self,n,p,e,c,ph)
        self.manager.transition.direction= "right"
        self.manager.current = "login_screen"



d=""
class TrainReservationScreen(Screen):
    check=[]
    def from_clicked(self,fro):
        TrainReservationScreen.check.append(fro)
    def to_clicked(self,to):
        TrainReservationScreen.check.append(to)
    def from_to(self,date):
        global_lists=globals()
        born = datetime.strptime(date, '%d %m %Y').weekday()
        global_lists["d"]=date
        result=backendproject.miniproject.gettraindetails(self,TrainReservationScreen.check[0],TrainReservationScreen.check[1],born)
        if type(result) == str: 
            self.manager.current = "TR_screen"
            
        else:
            self.manager.transition.direction = "left"
            self.manager.current = "TD_screen"

cl=""
seats=0
class TrainDetailsScreen(Screen):
    details=[]
    def spinner_clicked(self,name):
        trains={"SHIV GANGA EXPRESS":12559,"DECCAN EXPRESS":12560,"RAJDHANI EXPRESS":12581,"SHATABDI EXPRESS":12582}
        if name in trains.keys():
            TrainDetailsScreen.details.append(trains[name])

    def class_clicked(self,clas):
        globals_list=globals()
        classes={"SLEEPER":"seat_sleeper","AC1":"seat_first_class_AC","AC2":"seat_second_class_AC","AC3":"seat_third_class_AC"}
        globals_list["cl"]=classes[clas]

    def add_seats(self,seat):
        globals_list=globals()
        seat=int(seat)
        globals_list["seats"]=seat
        TrainDetailsScreen.details.append(seat)
        uname=globals_list["u"]
        date=globals_list["d"]
        TrainDetailsScreen.details.append(uname)
        TrainDetailsScreen.details.append(date)
        print(TrainDetailsScreen.details)
        backendproject.miniproject.insertticket(self,TrainDetailsScreen.details[0],TrainDetailsScreen.details[1],TrainDetailsScreen.details[2],TrainDetailsScreen.details[3])
        self.manager.transition.direction = "left"
        self.manager.current = "PD_screen"

    def show_trains(self):
        trains={12559:"SHIV GANGA EXPRESS",12560:"DECCAN EXPRESS",12581:"RAJDHANI EXPRESS",12582:"SHATABDI EXPRESS"}
        self.ids.tn.text="Available Trains: "
        if backendproject.miniproject.train_no !=[]:
            for a in backendproject.miniproject.train_no:
                self.ids.tn.text+=f"{trains[a]},"
            

class PassengerDetailsScreen(Screen):
    a=2
    details=[]
    def confirm(self,first,last,ag,phone):
        ag=int(ag)
        globals_list=globals()
        PassengerDetailsScreen.details.append(first)
        PassengerDetailsScreen.details.append(last)
        PassengerDetailsScreen.details.append(ag)
        PassengerDetailsScreen.details.append(phone)
        con=mysql.connector.connect(host="localhost",user="root",passwd="Bhadouria123",database="Train_Reservation")
        cur=con.cursor()
        cur.execute("select ticket_no from ticket order by ticket_no desc limit 1;")
        tno=cur.fetchone()
        globals_list["t_no"]=tno[0]
        con.commit()
        con.close()
        PassengerDetailsScreen.details.append(tno[0])
        cl=globals_list["cl"]
        PassengerDetailsScreen.details.append(cl)
        backendproject.miniproject.PassengerDetails(self,PassengerDetailsScreen.details)
        print(PassengerDetailsScreen.details)
        PassengerDetailsScreen.details=[]
        seats=globals_list["seats"]+1
        if PassengerDetailsScreen.a in range(2,seats):
            self.manager.current = "PD_screen"
            self.ids.PD.text=f"Passenger {PassengerDetailsScreen.a} Details"
            self.ids.fn.text=""
            self.ids.ln.text=""
            self.ids.age.text=""
            self.ids.phone.text=""
            PassengerDetailsScreen.a+=1
        else:
            self.manager.transition.direction = "left"
            self.manager.current= "Ticket_screen"
        
    
    def gender_clicked(self,gender):
        gen={"MALE":'M',"FEMALE":'F',"OTHERS":"O"}
        PassengerDetailsScreen.details.append(gen[gender])
t_no=0
class TicketDetailsScreen(Screen):
    def exit(self):
        quit()
    def show_ticket(self):
        tic=""
        globals_list=globals()
        tno=globals_list["t_no"]
        ticket=backendproject.miniproject.TicketDetails(self,tno)
        self.ids.ticket.text=f"tno\tseats d_of_journey\tpid\tfname\tlname\tsex\tpno  \tage\t  class\n"
        for a in ticket:
            for b in range(0,10):
                tic+=f"{a[b]}\t"
            self.ids.ticket.text+=f"{tic}\n"
            tic=""
    def cancel_ticket(self):
        globals_list=globals()
        tno=globals_list["t_no"]
        self.ids.ticket.text = ''
        backendproject.miniproject.CancelTicket(self,tno)


class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__=="__main__":
    MainApp().run()