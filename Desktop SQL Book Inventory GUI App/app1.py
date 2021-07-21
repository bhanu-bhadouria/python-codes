from tkinter import *
import backend

selected_row=()


window =Tk()
window.wm_title("Book Store")

def view_command():
    listbox.delete(0 ,END)
    for row in backend.view():
        listbox.insert(END,row)

def search_command():
    listbox.delete(0,END)
    for row in backend.search(title_text.get(),Author_text.get(),year_text.get(),ISBN_text.get()):
        listbox.insert(END,row)

def add_command():
    backend.insert(title_text.get(),Author_text.get(),year_text.get(),ISBN_text.get())
    view_command()

def  update_command():
    listbox.delete(0,END)
    backend.update(selected_row[0],title_text.get(),Author_text.get(),year_text.get(),ISBN_text.get())
    view_command()

def delete_command():
    global selected_row
    listbox.delete(0,END)
    backend.delete(selected_row[0])
    view_command()

def get_selected_index(event):
    global selected_row
    try:
        index = listbox.curselection()[0]
        selected_row = listbox.get(index)
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e1.insert(END,selected_row[1])
        e2.insert(END,selected_row[2])
        e3.insert(END,selected_row[3])
        e4.insert(END,selected_row[4])
    except IndexError:
        pass



l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

Author_text=StringVar()
e2=Entry(window,textvariable=Author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

ISBN_text=StringVar()
e4=Entry(window,textvariable=ISBN_text)
e4.grid(row=1,column=3)

listbox=Listbox(window,height=6,width=35)
listbox.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window,orient="vertical")
sb1.grid(row=2,column=2,rowspan=6)

sb2=Scrollbar(window,orient="horizontal")
sb2.grid(row=8,column=0,columnspan=2)

listbox.configure(yscrollcommand=sb1.set,xscrollcommand=sb2.set)
listbox.bind("<<ListboxSelect>>",func=get_selected_index)
sb1.configure(command=listbox.yview)
sb2.configure(command=listbox.xview)

b1=Button(window,text="View All",width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update Selected",width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete Selected",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)
window.mainloop()