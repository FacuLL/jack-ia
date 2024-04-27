from models.card import Card
from models.printer import Printer
from models.persona import Persona
from utils.cardsUtils import sumValues

class Dealer(Persona):
    cards = []
    
    def decide(self, printer = None):
        return sumValues(self.cards) < 17
    
    def appendCard(self, card: Card):
        self.cards.append(card)
    
    def resetCards(self):
        self.cards = []