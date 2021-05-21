def create():
    ID=int(input("pls enter an ID: "))
    pswd=input("pls create a password: ")
    temp={ID:pswd}
    login_details.update(temp)
    name=input("pls enter your name: ")
    gender=input("pls enter your gender(M/F): ")
    age=int(input("pls enter your age: "))
    salary=int(input("pls enter your salary: "))
    temp2={ID:{"name":name,"gender":gender,"age":age,"salary":salary}}
    personal_info.update(temp2)

def login():
    L_ID=int(input("ID: "))
    if(L_ID in login_details):
        L_pswd=input("password: ")
        if(L_pswd.__eq__(login_details[L_ID])):
            details=personal_info[L_ID]
            for value in details.items():
                print(value)
        else:
            print("incorect password\n")
            return
    else:
        print("ID does not exist\n")
        return


login_details={}
personal_info={}
choice=True
while(choice):
    print("\n1.create an ID\n2.login \n3.Exit\n")
    c=int(input())
    if(c==1):
        create()
    elif(c==2):
        login()
    elif(c==3):
        choice=False
    else:
        print("invalid input")
