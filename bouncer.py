age=int(input("pls enter your age to get into the pub: "))
if age !='':
    if (age>=18 and age<21):
        print("you can enter but have to wear wristband and cannot drink ")
    elif (age>=21):
        print("you can have drinks ")
    elif (age>0 and age<18):
        print("!!!!NO ENTRY!!!!")
    else:
        print("pls enter a valid age")
else:
    print("pls enter a valid age")
