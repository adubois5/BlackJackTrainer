from sklearn.utils import shuffle
from Card import *
import random

class CardLL:
    def __init__(self, _dataVal, _nextVal):
        self.data = _dataVal
        self.next = _nextVal
    def __str__(self):
        returnString = "List of Cards:\n"
        while self.next != None:
            returnString += self.data.__str__()
            self = self.next
        return returnString
    def __add__(self, other):
        if str(type(other)) == "<class '__main__.CardLL'>" or str(type(other)) == "<class 'CardLL.CardLL'>":
            # Get the last Card
            lastCard = self.getLastCard()
            # Next is the new head pointer
            lastCard.next = other
        elif str(type(other)) == "<class 'Card.Card'>":
            # Add new card into LL
            lastCard = self.getLastCard()
            lastCard.next = CardLL(other, lastCard.next)
        return self
    def addCard(self, _card):
        ll = CardLL(_card, None)
        self = ll + self
        return self

    def getLastCard(self):
        if self.next != None:
            while self.next.next != None:
                self = self.next
        return self
    def getBeforeLastCard(self):
        while self.next.next.next != None:
            self = self.next
        return self
    def removeCard(self):
        bflastCard = self.getBeforeLastCard()
        removedCard = bflastCard.next
        bflastCard.next = removedCard.next # Python handles memory?
        removedCard.next = CardLL(None, None)
        return removedCard
    def popCard(self):
        cardPopped = CardLL(self.data, CardLL(None, None))
        self.__dict__.update(self.next.__dict__)
        return cardPopped
    def shuffleList(self):
        cardList = self.getllToList()
        llNew = CardLL(None, None)
        cardList = shuffle(cardList)
        for card in cardList:
            llNew = llNew + card
        return llNew
    def getCard(self, other):
        pass
    def getllToList(self):
        cardList = list()
        if (self.next != None and self.next.next!= None):
            while self.next.next.next != None:
                cardList += [self.data]
                self = self.next
        return cardList


if __name__ == "__main__":
    ll = CardLL(None, None)
    print(ll)
    ll = ll.addCard(Card(2, "a"))
    print(ll)
    ll = ll + (Card(2, "b"))
    ll = ll.addCard(Card(2, "c"))
    ll = ll.addCard(Card(2, "d"))
    print(ll)
    print(ll.removeCard())
    print(ll)
    ll.popCard()
    print(ll)
    ll += Card(3, "a")
    ll += Card(4, "b")
    ll += Card(5, "c")
    ll += Card(6, "d")
    ll += Card(7, "e")
    ll += Card(8, "f")
    ll += Card(9, "h")
    ll += Card(1, "j")
    ll += Card(2, "k")
    ll += Card(3, "l")
    ll += Card(4, "o")
    print(ll)
    ll = ll.shuffleList()
    print(ll)