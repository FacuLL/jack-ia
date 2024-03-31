from models.card import Card
from models.persona import Persona
from utils.cardsUtils import sumValues, mapLetters

class Printer:
    def gameStart(self):
        print("Comienza el juego.")
    
    def roundStart(self):
        print("Comienza la ronda.")
    
    def chooseValue(self, card: Card):
        print("La carta que te toco es ", card.letter, ", debes elegir su valor. Valores posibles: ", card.values)
    
    def wrongValue(self):
        print("Valor incorrecto.")
    
    def printCards(self, player: Persona, dealer: Persona):
        print("Cartas del dealer: ", list(map(mapLetters, dealer.cards)), " Total: ", sumValues(dealer.cards))
        print("Cartas tuyas: ", list(map(mapLetters, player.cards)), " Total: ", sumValues(player.cards))
    
    def lostRound(self):
        print("Perdiste la ronda")
    
    def winnedRound(self):
        print("Ganaste la ronda")
    
    def tiedRound(self):
        print("Empataste la ronda")
    
    def gameFinish(self, win: int, lose: int, tie: int):
        print("Se termina la partida, no hay suficientes cartas para seguir.")
        print("Rondas ganadas: ", win)
        print("Rondas perdidas: ", lose)
        print("Rondas empatadas: ", tie)
