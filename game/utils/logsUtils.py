from datetime import datetime
import os
from models.enviroment import Enviroment

def createLogFile(algorithm, env: Enviroment, timesteps, obsDescription):
    logpath = "./Logs/"
    newest = max([f for f in os.listdir(logpath)], key=lambda x: os.stat(os.path.join(logpath,x)).st_birthtime)
    f = open(logpath + newest + "/info.txt","w+")
    f.writelines([
        "Date: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "Algorithm: " + algorithm,
        "Timesteps (Matches): " + str(timesteps),
        "Decks: " + str(env.ndecks),
        "Rewards (Win, Lose, Tie): " + str(env.winrew) + " " + str(env.loserew) + " 0",
        "Ignored rounds: " + str(env.ignoredRounds),
        "Observation space: " + obsDescription
    ])
    f.close()