class Card:
    def __init__(self, _value, _suit):
        # Definition of a card:
        self.value = _value
        self.suit = _suit

        # Create the faceup display of the card:
        self.faceUp = ("┌─────────┐" + "| {}       |" + "|         |" + "|    {}    |" + "|         |" + "|       {} |"+"└─────────┘").format(_value, _suit, _value)

        # Creates the facedown display of the card:
        self.facedown = "┌─────────┐" + "|         |" * 4 + "└─────────┘"
    def __str__ (self):
        print(self.value + " of " + self.suit)