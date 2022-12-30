from sklearn.utils import shuffle
from Card import *
from IterableLL import *

class CardLL:
    def __init__(self, _dataVal, _nextVal):
        self.data = _dataVal
        self.next = _nextVal
    def __str__(self):
        if (self.getSize() == 0):
            return "Empty Deck"
        returnString = "List of Cards:\n"
        for card in self:
            returnString += card.__str__()
        return returnString
    def __iter__(self):
        return IterableLL(self)
    def __add__(self, other):
        if str(type(other)) == "<class '__main__.CardLL'>" or str(type(other)) == "<class 'CardLL.CardLL'>":
                for card in other:
                    self = self + card
        elif str(type(other)) == "<class 'Card.Card'>":
            if self.getSize() == 0 and self.data == None:
                self.data = other
            else:
                # Add new card into LL
                lastCard = self.getLastCard()
                lastCard.next = CardLL(other, lastCard.next)
        else:
            SystemExit("Can only add Cards or CardLL to a CardLL")
        return self
    def addCard(self, _card):
        self = self + _card
        return self

    def getLastCard(self):
        if self != None:
            while self.next != None:
                self = self.next
        return self
    def getBeforeLastCard(self):
        if (self.next != None):
            while self.next.next != None:
                self = self.next
        return self
    def removeCard(self):
        if (self.getSize() == 0):
            removedCard = self.data
            self.data = None
        else:
            bflastCard = self.getBeforeLastCard()
            removedCard = bflastCard.next
            bflastCard.next = removedCard.next # Python handles memory?
            removedCard.next = CardLL(None, None)
        return removedCard
    def popCard(self):
        cardPopped = CardLL(self.data, CardLL(None, None))
        self.__dict__.update(self.next.__dict__)
        return cardPopped
    def shuffleCardLL(self):
        cardList = self.getllToList()
        llNew = CardLL(None, None)
        cardList = shuffle(cardList)
        for card in cardList:
            llNew = llNew + card
        return llNew
    def getllToList(self):
        cardList = list()
        if (self.next != None):
            while self.next != None:
                cardList += [self.data]
                self = self.next
        return cardList
    def getSize(self):
        counter = 0
        if (self.data != None):
            counter += 1
        if (self.next != None):
            while self.next != None:
                counter += 1
                self = self.next
        return counter


if __name__ == "__main__":
    ll = CardLL(None, None)
    print(ll)
    print(ll.getSize())
    ll = ll.addCard(Card(2, "a"))
    print(ll)
    print(ll.getSize())
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
    for card in ll:
        print(card)
    print(ll.getSize())
    print(ll)
    ll = ll.shuffleCardLL()
    print(ll)