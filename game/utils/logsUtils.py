from datetime import datetime
import os
from models.enviroment import Enviroment

from stable_baselines3.common.vec_env import DummyVecEnv

def createLogFile(algorithm, envWrap: DummyVecEnv, timesteps, obsDescription):
    logpath = "./Logs/"
    env = envWrap.envs[0].unwrapped
    newest = max([f for f in os.listdir(logpath)], key=lambda x: os.stat(os.path.join(logpath,x)).st_birthtime)
    f = open(logpath + newest + "/info.txt","w+")
    lines = [
        "Date: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "Algorithm: " + algorithm,
        "Timesteps (Matches): " + str(timesteps),
        "Decks: " + str(env.ndecks),
        "Rewards (Win, Lose, Tie): " + str(env.winrew) + " " + str(env.loserew) + " 0",
        "Ignored cards: " + str(env.ignoredCards),
        "Observation space: " + obsDescription
    ]
    f.writelines(line + '\n' for line in lines)
    f.close()