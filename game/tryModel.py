import time
import os
from models.enviroment import Enviroment
from models.player import Player
from models.dealer import Dealer
from stable_baselines3 import PPO, DQN, A2C

# General parameters
mazos = 8
episodes = 50000
timeFreq = 1000
env = Enviroment(mazos, Player(), Dealer())

# Load model
model_path = os.path.join("RL_Models", "DQN_20240520-152717", "best_model")
model = DQN.load(model_path, env=env)

# Variables
wins = 0
loses = 0

firstRoundsWins = 0
firstRoundsLoses = 0
lastRoundsWins = 0
lastRoundsLoses = 0

timeAverage = 0
times = []

for episode in range(episodes):
    obs, info = env.reset()
    done = False
    score = 0
    ronda = 0

    roundResults = []

    while not done:
        ronda+=1
        start = time.time()
        action = model.predict(obs)[0]
        end = time.time()
        if ((episode+1) % timeFreq == 0):
            times.push(end - start)
        obs, reward, done, truncated, info = env.step(action)
        score+=reward
        if "result" in info:
            if info["result"] == "win":
                wins+=1
                roundResults.append("win")
            if info["result"] == "lose":
                loses+=1
                roundResults.append("lose")
    firstRounds = roundResults[:10]
    lastRounds = roundResults[-10:]
    for result in firstRounds:
        if result == "win":
            firstRoundsWins+=1
        if result == "lose":
            firstRoundsLoses+=1
    for result in lastRounds:
        if result == "win":
            lastRoundsWins+=1
        if result == "lose":
            lastRoundsLoses+=1

    print("Partida ", episode+1, " Puntaje ", score)
print("Promedio victorias en " + episodes + " partidas: " + str(wins / (wins + loses) * 100) + "%")
print("Promedio victorias en primeras 10 rondas: " + str(firstRoundsWins / (firstRoundsWins + firstRoundsLoses) * 100) + "%")
print("Promedio victorias en ultimas 10 rondas: " + str(lastRoundsWins / (lastRoundsWins + lastRoundsLoses) * 100) + "%")
print("Promedio tiempo de " + timeFreq + " decisiones: " + str(sum(times) / len(times)) + " segundos")
env.close()