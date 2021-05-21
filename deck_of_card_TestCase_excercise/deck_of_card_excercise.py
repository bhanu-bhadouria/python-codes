import random
class Card:
    def __init__(self,suit,value):
            self.suit=suit
            self.value=value
    def __repr__(self): 
        return f"{self.value} of {self.suit}"

class Deck:

    def __init__(self):
        suits=["Hearts", "Diamonds", "Clubs", "Spades"]
        values=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards=[Card(s,v) for s in suits for v in values]
        random.shuffle(self.cards)
    def count(self):
        return f"{len(self.cards)} remaining in deck"
    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"
    def _deal(self,num):
        card=[]
        if(len(self.cards)==0):
            raise ValueError("All cards have been dealt")
        elif(len(self.cards)<=num):
            remaining=len(self.cards)
            while(remaining>0):
                card.append(self.cards.pop())
                remaining-=1
        elif(len(self.cards)>=num):
            while(num>0):
                card.append(self.cards.pop())
                num-=1
        return card
    def shuffle_deck(self):
        if(len(self.cards)==52):
            random.shuffle(self.cards)
            print("shuffled successfully")
        else:
            raise ValueError("only full deck cards can be shuffled")
    def deal_card(self):
        dealt=self._deal(1)
        print(f"dealt with {dealt}")
    def deal_hand(self,number):
        dealt=self._deal(number)
        print(f"dealt with {dealt}")
    

d=Deck()
d.shuffle_deck()
d.deal_card()
d.deal_hand(50)
d.deal_card()
print(d.cards)
print(d)
d.deal_card()