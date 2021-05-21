import random
print("ROCK-PAPER-SCISSOR")
player1=input("player 1 enter your choice: ")
computer=random.randint(0,2)
if(computer==0):
    computer="rock"
elif(computer==1):
    computer="paper"
elif(computer==2):
    computer="scissor"
print(f"compter choice: {computer}")
player1=player1.lower()
if(player1=="rock"):
    if(computer=="rock"):
        print("TIE")
    elif(computer=="paper"):
        print("computer wins")
    elif(computer=="scissor"):
        print("player 1 wins")
elif(player1=="paper"):
    if(computer=="rock"):
        print("player 1 wins")
    elif(computer=="paper"):
        print("TIE")
    elif(computer=="scissor"):
        print("computer wins")
elif(player1=="scissor"):
    if(computer=="rock"):
        print("computer wins")
    elif(computer=="paper"):
        print("player 1 wins")
    elif(computer=="scissor"):
        print("TIE")
else:
    print("invalid input")