from models.card import Card
import numpy as np

def makeDeck():
    cards = []
    suits = ["D", "S", "H", "C"]
    letters = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    values = [[1, 11], [2], [3], [4], [5], [6], [7], [8], [9], [10], [10], [10], [10]]
    for suit in suits:
        for idx, letter in enumerate(letters):
            cards.append(Card(letter, suit, values[idx], idx))
    return cards

def multiplyCards(cards: list[Card], times: int):
    aux = []
    for card in cards:
        for i in range(times):
            aux.append(Card(card.letter, card.suit, card.values, card.position))
    return aux

def sumValues(cards: list[Card]):
    result = 0
    aux = cards.copy()
    aux.sort(key=lambda x: len(x.values))
    for card in cards:
        if len(card.values) == 1:
            result += card.values[0]
        else:
            if result + max(card.values) <= 21:
                result += max(card.values)
            else:
                result += min(card.values)
    return result

def mapLetters(card: Card):
    return card.letter

def positionSum(cards: list[Card]):
    res = np.empty(13, dtype=int)
    res.fill(0)
    for card in cards:
        res[card.position]+=1
    return res

def elegirMazos():
	mazos = 0
	while mazos < 2 or mazos > 8:
		mazos = int(input("Elige la cantidad de mazos (2-8): "))
		if mazos < 2 or mazos > 8:
			print("La cantidad de mazos es incorrecta.")
	return mazos