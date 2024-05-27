import time
import os
from models.enviroment import Enviroment
from models.player import Player
from models.dealer import Dealer
from stable_baselines3 import PPO, DQN, A2C

# General parameters
mazos = 8
episodes = 100
timeFreq = 1
env = Enviroment(mazos, Player(), Dealer())

# Load model
model_path = os.path.join("RL_Models", "A2C_20240526-194244", "best_model")
model = A2C.load(model_path, env=env)

# Variables
wins = 0
loses = 0

firstRoundsWins = 0
firstRoundsLoses = 0
lastRoundsWins = 0
lastRoundsLoses = 0

totalTimes = []
seconds = 0

timestepsCount = 0

for episode in range(episodes):
    obs, info = env.reset()
    done = False
    score = 0
    round = 0

    roundResults = []

    while not done:
        timestepsCount+=1
        round+=1
        start = time.time()
        action = model.predict(obs)[0]
        end = time.time()
        seconds += (end - start)
        if (timestepsCount % timeFreq == 0):
            totalTimes.append(seconds)
            print("Tiempo de " + str(timeFreq) + " decisiones: " + str(seconds) + " segundos")
            seconds = 0
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

    print("Partida ", str(episode+1), " Puntaje ", str(score))
print("Promedio victorias en " + str(episodes) + " partidas: " + str(wins / (wins + loses) * 100) + "%")
print("Promedio victorias en primeras 10 rondas: " + str(firstRoundsWins / (firstRoundsWins + firstRoundsLoses) * 100) + "%")
print("Promedio victorias en ultimas 10 rondas: " + str(lastRoundsWins / (lastRoundsWins + lastRoundsLoses) * 100) + "%")
print("Promedio tiempo de " + str(timeFreq) + " decisiones: " + str(sum(totalTimes) / len(totalTimes)) + " segundos")
env.close()