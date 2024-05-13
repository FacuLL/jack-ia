from datetime import datetime
import os
from models.enviroment import Enviroment

from stable_baselines3.common.vec_env import DummyVecEnv

def createLogFile(algorithm, env: DummyVecEnv, timesteps, obsDescription):
    logpath = "./Logs/"
    newest = max([f for f in os.listdir(logpath)], key=lambda x: os.stat(os.path.join(logpath,x)).st_birthtime)
    f = open(logpath + newest + "/info.txt","w+")
    f.writelines([
        "Date: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "Algorithm: " + algorithm,
        "Timesteps (Matches): " + str(timesteps),
        "Decks: " + str(env.envs[0].ndecks),
        "Rewards (Win, Lose, Tie): " + str(env.winrew) + " " + str(env.envs[0].loserew) + " 0",
        "Ignored rounds: " + str(env.envs[0].ignoredRounds),
        "Observation space: " + obsDescription
    ])
    f.close()