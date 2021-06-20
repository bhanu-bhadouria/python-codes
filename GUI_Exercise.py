from tkinter import *

window=Tk()

def kg_to_grams():
    grams=str(float(kg.get())*1000)+" grams"
    t1.delete("1.0",END)
    t1.insert(END, grams)
    kg_to_pounds()
def kg_to_pounds():
    pounds=str(float(kg.get())*2.20462)+" pounds"
    t2.delete("1.0",END)
    t2.insert(END,pounds)
    kg_to_ounces()
def kg_to_ounces():
    ounces=str(float(kg.get())*35.274)+" ounces"
    t3.delete("1.0",END)
    t3.insert(END,ounces)

l1=Label(window,text="kg")
l1.grid(row=0,column=1)

kg=StringVar()
e1=Entry(window,textvariable=kg)
e1.grid(row=0,column=0)

b1=Button(window,text="convert",command=kg_to_grams)
b1.grid(row=0,column=2)

t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)

window.mainloop()