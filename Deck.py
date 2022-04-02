from typing import Type
from Card import *
from CardLL import CardLL

class Deck:
    def __init__(self): 
        self.cardLL = CardLL()
    
    def __add__(self,other):
        try:
            if (type(self) == Card() and type(other) == Deck() or type(other) == Card() and type(self) == Deck()):
                self.cardLL.addCard(other)
            elif type(self) == Deck() and type(other) == Deck():
                card = other.cardLL.getCard()
                while card != None:
                    self.cardLL.addCard(card)
                    other.cardLL.popCard() # Might cause pointer issues
                    card = card.next
            else:
                raise TypeError
        except TypeError:
            print("Both objects must be decks or a card and a deck")


    def __str__(self):
        card = self.cardLL.getCard()
        while card != None:
            print(card)
            card = card.next
            

    def createDeck(self):
        # Generates linked list of 52 cards:
        arrayOfCards = ['2'] + ['3'] + ['4'] + ['5'] + ['6'] + ['7'] + ['8'] + ['9'] + ['10'] + ['J'] + ['Q'] + ['K'] + ['A'] 
        
        for element in arrayOfCards:
            # Adds one copy of every suit
            suitList =["♣","♦","♥","♠"]
            cardsToAdd = [Card(element, _suit) for _suit in suitList]
            for card in cardsToAdd:
                self.cardLL.addCard(card)