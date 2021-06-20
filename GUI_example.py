from tkinter import *

window = Tk()

def km_to_miles():
    km=float(e1.get())*1.6
    t1.insert(END,(str(km)+" miles"))


b1 = Button(window,text="miles",command=km_to_miles)
b1.grid(row=0,column=0)

value=StringVar()
e1 = Entry(window,textvariable=value)
e1.grid(row=0,column=1)

t1 = Text(window,height=1,width=30)
t1.grid(row=0,column=2)

window.mainloop()
