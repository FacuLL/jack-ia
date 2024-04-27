from models.card import Card
from models.printer import Printer
from models.persona import Persona

class Player(Persona):
    def __init__(self):
        self.cards = []
    
    def decide(self, printer: Printer  = None):
        decision = None
        posibilities = [0, 1]
        while decision not in posibilities:
            decision = int(input("¿Qué decides hacer? 0-Plantarse 1-Tomar: "))
            if decision not in posibilities:
                if (printer): 
                    printer.wrongValue()
        return decision != 0
    
    def appendCard(self, card: Card):
        self.cards.append(card)
    
    def resetCards(self):
        self.cards = []