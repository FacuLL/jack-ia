from datetime import datetime
from models.enviroment import Enviroment

def createLogFile(logname, algorithm, env: Enviroment, timesteps, obsDescription):
    f = open("./Logs/" + logname + "/info.txt","w+")
    f.write("Date: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    f.write("Algorithm: " + algorithm)
    f.write("Timesteps (Matches): " + timesteps)
    f.write("Decks: " + env.ndecks)
    f.write("Rewards (Win, Lose, Tie): " + env.winrew + " " + env.loserew + " 0")
    f.write("Ignored rounds: " + env.ignoredRounds)
    f.write("Observation space: " + obsDescription)
    f.close()