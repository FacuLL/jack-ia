from abc import ABC, abstractmethod

from models.card import Card

class Persona(ABC):
    @abstractmethod
    def decide(self, printer = None):
        pass
    
    def appendCard(self, card: Card):
        self.cards.append(card)
    
    def resetCards(self):
        cards = []