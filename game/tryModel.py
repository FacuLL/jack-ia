import os
from models.enviroment import Enviroment
from models.player import Player
from models.dealer import Dealer
from stable_baselines3 import PPO, DQN, A2C

mazos = 8
episodes = 1000
env = Enviroment(mazos, Player(), Dealer(), ignoredCards=350)

model_path = os.path.join("RL_Models", "DQN_5", "best_model")
model = DQN.load(model_path, env=env)

wins = 0
loses = 0

for episode in range(episodes):
    obs, info = env.reset()
    done = False
    score = 0

    while not done:
        env.render()
        action = model.predict(obs)[0]
        obs, reward, done, truncated, info = env.step(action)
        score+=reward
        if "result" in info:
            if info["result"] == "win":
                wins+=1
            if info["result"] == "lose":
                loses+=1
    print("Partida ", episode+1, " Puntaje ", score)
print("Winrate " + str(wins / (wins + loses) * 100))
env.close()