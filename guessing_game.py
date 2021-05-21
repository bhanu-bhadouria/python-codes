import random
choice="y"
while(choice=="y"):
    number=random.randint(1,10)
    guessed_number=0
    while(number!=guessed_number):
        guessed_number=int(input("pls enter your guess between 1 & 10: "))
        if(guessed_number>=1 and guessed_number<=10):
            if(guessed_number<number):
                print("too low")
            elif(guessed_number>number):
                print("too high")
            elif(guessed_number==number):
                print("YOU GUESSED IT!!!!")
                break
        else:
            print("not in range 1-10")
    choice=input("do you wish to continue(y/n): ")

        
        
            