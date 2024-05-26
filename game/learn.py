from datetime import datetime
import os
from utils.logsUtils import createLogFile
from utils.callbacks import LoggingCallback
from models.enviroment import Enviroment
from stable_baselines3.common.monitor import Monitor
from models.player import Player
from models.dealer import Dealer
from stable_baselines3 import PPO, DQN, A2C
from stable_baselines3.common.callbacks import EvalCallback, StopTrainingOnNoModelImprovement, CallbackList
# import wandb
# from wandb.integration.sb3 import WandbCallback

timesteps = 4000000
mazos = 8

# wandb.init(
#     project="jack-ia",
#     config={
#         "env": "Blackjack",
#         "total_timesteps": timesteps,
#         "policy_type": "MultiInputPolicy",
#         "win-lose-tie rewards": "1 -1 0",
#         "observation_space": "cartas completas dealer-player-previas",
#         "decks": mazos
#     },
#     sync_tensorboard=True
# )

default_env = Monitor(Enviroment(mazos, Player(), Dealer()))
winrew_env = Monitor(Enviroment(mazos, Player(), Dealer(), winrew=2))
both_env = Monitor(Enviroment(mazos, Player(), Dealer(), winrew=2, ignoredCards=50))
ignored_env_250 = Monitor(Enviroment(mazos, Player(), Dealer(), ignoredCards=250))

log_path = os.path.join("Logs")

models = [
    PPO("MultiInputPolicy", default_env, verbose=1, tensorboard_log=log_path),
    A2C("MultiInputPolicy", default_env, verbose=1, tensorboard_log=log_path),
]

for model in models:
    algorithm = model.__class__.__name__
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    save_path = os.path.join("RL_Models", algorithm + "_" + timestamp)

    log_freq = 1
    if algorithm == "DQN": 
        log_freq = 250
    if algorithm == "A2C":
        log_freq = 100

    stop_callback = StopTrainingOnNoModelImprovement(
        max_no_improvement_evals=100000,
        min_evals=timesteps,
        verbose=1
    )
    eval_callback = EvalCallback(model.env,
        callback_after_eval=stop_callback,
        eval_freq=10000,
        best_model_save_path=save_path,
        verbose=1
    )
    logging_callback = LoggingCallback(verbose=1, log_freq=log_freq)
    # wandb_callback = WandbCallback(verbose=2, log="all", gradient_save_freq=100)
    callbacks = CallbackList([logging_callback, eval_callback])
    
    model.learn(timesteps, callback=callbacks)
    createLogFile(algorithm, model.env, timesteps, "Cartas previas, player, dealer")

# wandb.finish()