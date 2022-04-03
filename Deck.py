from typing import Type
from Card import *
from CardLL import CardLL

class Deck:
    def __init__(self): 
        self.cardLL = CardLL(None, None)
    
    def __add__(self,other):
        try:
            if type(other) == Card():
                self.cardLL.addCard(other)
            elif type(other) == Deck():
                card = other.cardLL.getCard()
                while card != None:
                    self.cardLL.addCard(card)
                    other.cardLL.popCard() # Might cause pointer issues
                    card = card.next
            else:
                raise TypeError
        except TypeError:
            print("Both objects must be decks or a card and a deck")
        return self

    def __str__(self):
        returnString = ""
        returnString += self.cardLL.__str__()
        return returnString
    def shuffleDeck(self):
        self.cardLL = self.cardLL.shuffleList()
        return self
    def createDeck(self):
        # Generates linked list of 52 cards:
        arrayOfCards = ['2'] + ['3'] + ['4'] + ['5'] + ['6'] + ['7'] + ['8'] + ['9'] + ['10'] + ['J'] + ['Q'] + ['K'] + ['A'] 
        
        for element in arrayOfCards:
            # Adds one copy of every suit
            suitList =["♣","♦","♥","♠"]
            cardsToAdd = [Card(element, _suit) for _suit in suitList]
            for card in cardsToAdd:
                self.cardLL = self.cardLL.addCard(card)
        return self

if __name__ == "__main__":
    deck1 = Deck()
    deck1 = deck1.createDeck()
    print(deck1)
    deck1 = deck1.shuffleDeck()
    print(deck1)