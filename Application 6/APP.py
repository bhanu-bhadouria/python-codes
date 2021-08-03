from hoverable import HoverBehavior
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from pathlib import Path
from datetime import datetime
import random
import json,glob

Builder.load_file("design.kv")

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "Sign_up_screen"

    def login(self,uname,pword):
        with open("users.json") as file:
            users = json.load(file)
        if uname in users and users[uname]["password"] == pword:
            self.manager.current = "login_screen_success"
        else:
            self.ids.login_wrong.text = "Wrong username or password"
    def forgot_pwd(self,uname):
        with open("users.json") as file:
            users=json.load(file)
        if uname in users:
            self.ids.login_wrong.text ="HINT: "+ users[uname]["hint"]
        else:
            self.ids.login_wrong.text = "HINT: username incorrect"
class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_user(self,uname,pword,hinttext):
        with open("users.json") as file:
            users = json.load(file)
        users[uname] = {"username": uname,"password": pword,"hint": hinttext, "created":datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

        with open("users.json","w") as file:
            json.dump(users, file)
        self.manager.current = "Sign_up_screen_success"

class SignUpSuccess(Screen):
    def back_home(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

class LoginScreenSuccess(Screen):
    def Log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"
    
    def get_quote(self,feel):
        feel=feel.lower()
        available_feeling = glob.glob("Quotes/*txt")
        available_feeling = [Path(filename).stem for filename in available_feeling]

        if feel in available_feeling:
            with open(f"Quotes/{feel}.txt") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        
        else:
            self.ids.quote.text = "try another feeling"

class ImageButton( ButtonBehavior, HoverBehavior, Image):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__=="__main__":
    MainApp().run()