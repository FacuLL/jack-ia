import random
import numpy as np
from gymnasium import Env
from gymnasium.spaces import Discrete, Dict, MultiDiscrete

from models.persona import Persona
from models.player import Player
from utils.cardsUtils import makeDeck, multiplyCards, sumValues, positionSum

class Enviroment(Env):
    def __init__(self, ndecks, player: Player, dealer, winrew = 1, loserew = -1, ignoredCards = 0):
        self.action_space = Discrete(2) # Hit or pass
        discreteArray = np.empty(13)
        discreteArray.fill(ndecks*4+1)
        self.observation_space = Dict({
            "dealer": MultiDiscrete(discreteArray),
            "player": MultiDiscrete(discreteArray),
            "cards": MultiDiscrete(discreteArray)
        })
        self.ndecks = ndecks
        self.ignoredCards = ignoredCards
        self.cards = multiplyCards(makeDeck(), self.ndecks)
        random.shuffle(self.cards)
        self.previousCards = []
        if self.ignoredCards > 0:
            self.previousCards = self.cards[:self.ignoredCards-1]
            self.cards = self.cards[self.ignoredCards:]
        self.dealer = dealer
        self.player = player
        self.winrew = winrew
        self.loserew = loserew

    def step(self, action):
        reward = 0
        info = {}
        done = False
        truncated = False
        #HIT
        if action==1: 
            self.giveCard(self.player)
            if self.hasLost(self.player):
                reward = self.loserew
                info["result"] = "lose"
                self.resetCards()
                done = self.firstHand()
            state = self.generateState()
            return state, reward, done, truncated, info
        # PASS
        if not self.personaDecides(self.dealer):
            reward = self.winrew
            info["result"] = "win"
            self.resetCards()
            done = self.firstHand()
            state = self.generateState()
            return state, reward, done, truncated, info
        if sumValues(self.player.cards) > sumValues(self.dealer.cards):
            reward = self.winrew
            info["result"] = "win"
        elif sumValues(self.player.cards) < sumValues(self.dealer.cards):
            reward = self.loserew
            info["result"] = "lose"
        else:
            info["result"] = "tie"
        self.resetCards()
        done = self.firstHand()
        state = self.generateState()
        return state, reward, done, truncated, info

    def render(self):
        pass

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        info = {}
        self.resetCards()
        self.previousCards = []
        self.cards = multiplyCards(makeDeck(), self.ndecks)
        random.shuffle(self.cards)
        if self.ignoredCards > 0:
            self.previousCards = self.cards[:self.ignoredCards-1]
            self.cards = self.cards[self.ignoredCards:]
        self.firstHand()
        state = self.generateState()
        return state, info
    
    def generateState(self):
        state = {
            "player": positionSum(self.player.cards),
            "dealer": positionSum(self.dealer.cards),
            "cards": positionSum(self.previousCards)
        }
        return state

    def giveCard(self, persona: Persona):
        card = self.cards.pop(0)
        persona.appendCard(card)
        self.previousCards.append(card)

    def firstHand(self):
        if len(self.cards) >= 40:
            for i in range(2):
                self.giveCard(self.player)
                self.giveCard(self.dealer)
            return False
        return True

    def hasLost(self, persona: Persona):
        return sumValues(persona.cards) > 21

    def resetCards(self):
        self.dealer.resetCards()
        self.player.resetCards()

    def personaDecides(self, persona: Persona):
        hit = True
        while hit:
            if self.hasLost(persona):
                return False
            hit = persona.decide()
            if hit:
                self.giveCard(persona)
        return True