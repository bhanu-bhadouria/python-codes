from random import random
def flip_coin():
    r=random()
    if(r>0.5):
        return "heads"
    else:
        return "tails"

print(flip_coin())
