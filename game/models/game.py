import random
from models.printer import Printer
from models.persona import Persona
from utils.cardsUtils import makeDeck, multiplyCards, sumValues, mapLetters

class Game:
    def __init__(self, ndecks: int, player: Persona, dealer: Persona, printer: Printer):
        self.ndecks = ndecks
        self.cards = multiplyCards(makeDeck(), self.ndecks)
        random.shuffle(self.cards)
        self.printer = printer
        self.player = player
        self.dealer = dealer
        self.winCount = 0
        self.tieCount = 0
        self.loseCount = 0

    def giveCard(self, persona: Persona):
        card = self.cards.pop(0)
        persona.appendCard(card)

    def firstHand(self):
        for i in range(2):
            self.giveCard(self.player)
            self.giveCard(self.dealer)

    def hasLost(self, persona: Persona):
        return sumValues(persona.cards) > 21

    def resetCards(self):
        self.dealer.resetCards()
        self.player.resetCards()
    
    def personaDecides(self, persona: Persona, printAll: bool = False):
        hit = True
        while hit:
            if self.hasLost(persona):
                self.printer.printCards(self.player, self.dealer)
                return False
            hit = persona.decide(self.printer)
            if hit:
                self.giveCard(persona)
            if printAll:
                self.printer.printCards(self.player, self.dealer)
        if not printAll:
            self.printer.printCards(self.player, self.dealer)
        return True

    def startRound(self):
        self.printer.roundStart()
        print(list(map(mapLetters, self.cards)))
        self.firstHand()
        self.printer.printCards(self.player, self.dealer)
        if not self.personaDecides(self.player, True):
            return "lose"
        if not self.personaDecides(self.dealer):
            return "win"
        if sumValues(self.player.cards) > sumValues(self.dealer.cards):
            return "win"
        elif sumValues(self.player.cards) < sumValues(self.dealer.cards):
            return "lose"
        else:
            return "tie"

    def startGame(self):
        self.printer.gameStart()
        while len(self.cards) >= 40:
            match self.startRound():
                case "win":
                    self.printer.winnedRound()
                    self.winCount += 1
                case "lose":
                    self.printer.lostRound()
                    self.loseCount += 1
                case "tie":
                    self.printer.tiedRound()
                    self.tieCount += 1
            self.resetCards()
        self.printer.gameFinish(self.winCount, self.loseCount, self.tieCount)
            