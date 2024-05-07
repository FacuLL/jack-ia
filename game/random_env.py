from models.enviroment import Enviroment
from models.player import Player
from models.dealer import Dealer

mazos = 8
episodes = 5
env = Enviroment(mazos, Player(), Dealer())
for episode in range(episodes):
    obs, info = env.reset()
    done = False
    score = 0

    while not done:
        env.render()
        action = env.action_space.sample()
        obs, reward, done, truncated, info = env.step(action)
        score+=reward
    print("Partida ", episode+1, " Puntaje ", score, " Winrate ", info["winrate"], "%")
env.close()