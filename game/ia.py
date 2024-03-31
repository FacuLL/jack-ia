from utils.cardsUtils import elegirMazos
from models.game import Game
from models.player import Player
from models.dealer import Dealer
from models.printer import Printer

#TODO: REPROGRAMAR PARA LA IA
game = Game(elegirMazos(), Player(), Dealer(), Printer())
game.startGame()