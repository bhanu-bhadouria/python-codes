from termcolor import colored
from pyfiglet import figlet_format

def convert(s,co="magenta"):
    print(colored(figlet_format(s),color=co))

ss=input("pls enter the string : ")
c=input("pls enter the color : ")
valid_colors=("red","green","magenta","blue","yellow","cyan")
if c not in valid_colors:
    convert(ss)
else:
    convert(ss,c)