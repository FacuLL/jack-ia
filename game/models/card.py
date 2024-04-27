class Card:
    def __init__(self, letter: str, suit: str, values: list[int], position):
        self.letter = letter
        self.suit = suit
        self.values = values
        self.position = position