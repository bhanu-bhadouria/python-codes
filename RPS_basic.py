
print("ROCK-PAPER-SCISSOR")
player1=input("player 1 enter your choice: ")
for a in range(1,31):
    print("!!!NO CHEATING!!!")
player2=input("player 2 enter your choice: ")
player1=player1.lower()
player2=player2.lower()
if(player1=="rock"):
    if(player2=="rock"):
        print("TIE")
    elif(player2=="paper"):
        print("player 2 wins")
    elif(player2=="scissor"):
        print("player 1 wins")
elif(player1=="paper"):
    if(player2=="rock"):
        print("player 1 wins")
    elif(player2=="paper"):
        print("TIE")
    elif(player2=="scissor"):
        print("player 2 wins")
elif(player1=="scissor"):
    if(player2=="rock"):
        print("player 2 wins")
    elif(player2=="paper"):
        print("player 1 wins")
    elif(player2=="scissor"):
        print("TIE")
else:
    print("invalid input")