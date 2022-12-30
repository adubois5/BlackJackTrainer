class IterableLL:
    def __init__(self, _cardLL):
        self.cardLL = _cardLL
        self.cardIdx = 0
    def __next__(self):
        if (self.cardLL == None or self.cardLL.data == None):
            raise StopIteration
        if self.cardIdx > self.cardLL.getSize():
            raise StopIteration
        result = self.cardLL.data
        self.cardLL = self.cardLL.next
        return result