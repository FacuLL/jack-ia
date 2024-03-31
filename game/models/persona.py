from abc import ABC, abstractclassmethod

from models.card import Card

class Persona(ABC):
    @abstractclassmethod
    def decide(self, printer):
        pass
    
    def appendCard(self, card: Card):
        self.cards.append(card)
    
    def resetCards(self):
        cards = []