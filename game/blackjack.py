import random

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def elegirMazos():
	mazos = 0
	while mazos < 2 or mazos > 8:
		mazos = int(input("Elige la cantidad de mazos (2-8): "))
		if mazos < 2 or mazos > 8:
			print("La cantidad de mazos es incorrecta.")
	return mazos

def multiplicarCartas(cartas, veces):
	aux = []
	for j in cartas:
	    for i in range(veces):
	        aux.append(j)
	return aux

def decidirValor(posibles, decidePlayer):
	if decidePlayer:
		valor = None
		while valor not in posibles:
			valor = int(input("La carta que te toco es un Ás, ¿Qué valor decides darle? 1/11: "))
			if valor not in posibles:
				print("El valor ingresado es incorrecto.")
		return valor
	else:
		#CAMBIAR POR LAS REGLAS QUE USA EL DEALER PARA DECIDIR
		return posibles[0]

def darCarta(cartas, persona, decidePlayer=False):
	carta = cartas.pop(0)
	if (carta == 1):
		carta = decidirValor([1, 11], decidePlayer)
	persona.append(carta)

def primeraMano(cartas, player, dealer):
	print("Comienza el juego. Se reparten las cartas.")
	for i in range(2):
		darCarta(cartas, player, True)
		darCarta(cartas, dealer, False)

def imprimirCartas(player, dealer):
	print("Cartas del dealer: ", dealer, " Total: ", sum(dealer))
	print("Cartas tuyas: ", player, " Total: ", sum(player))

def playerDecide():
	# FALTA TERMINAR ESTO
	input("¿Qué decides hacer? 1-Tomar 2-Plantarse")

def startGame():
	mazos = elegirMazos()
	cartas = multiplicarCartas(valores, 4*mazos)
	random.shuffle(cartas)
	dealer = []
	player = []
	primeraMano(cartas, player, dealer)
	imprimirCartas(player, dealer)
	playerDecide()
	# Y FALTA SEGUIR TODO EL JUEGO
	
startGame()