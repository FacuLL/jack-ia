import os
from models.enviroment import Enviroment
from models.player import Player
from models.dealer import Dealer
from stable_baselines3 import PPO

mazos = 8
episodes = 5
env = Enviroment(mazos, Player(), Dealer())

model_path = os.path.join("RL_Models", "PPO", "best_model")
model = PPO.load(model_path, env=env)

for episode in range(episodes):
    obs, info = env.reset()
    done = False
    score = 0

    while not done:
        env.render()
        action = model.predict(obs)
        obs, reward, done, truncated, info = env.step(action)
        score+=reward
    print("Partida ", episode+1, " Puntaje ", score)
env.close()