class Card:
    def __init__(self, _value, _suit):
        # Definition of a card:
        self.value = _value
        self.suit = _suit

        # Create the faceup display of the card:
        self.faceUp = ("┌─────────┐" + "\n| {}       |" + "\n|         |" + "\n|    {}    |" + "\n|         |" + "\n|       {} |"+"\n└─────────┘").format(_value, _suit, _value)

        # Creates the facedown display of the card:
        self.facedown = "\n┌─────────┐" + "\n|         |" * 4 + "\n└─────────┘"
    def __str__ (self):
        returnString = str(self.value) + " of " + self.suit + "\n"
        return returnString