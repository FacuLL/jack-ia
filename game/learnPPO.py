import os
from utils.callbacks import LoggingCallback
from models.enviroment import Enviroment
from stable_baselines3.common.monitor import Monitor
from models.player import Player
from models.dealer import Dealer
from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import EvalCallback, StopTrainingOnNoModelImprovement, CallbackList
import wandb
from wandb.integration.sb3 import WandbCallback

timesteps = 100000
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

log_path = os.path.join("Logs")
save_path = os.path.join("RL_Models", "PPO")

env = Monitor(Enviroment(mazos, Player(), Dealer()))

stop_callback = StopTrainingOnNoModelImprovement(
    max_no_improvement_evals=100000,
    min_evals=timesteps,
    verbose=1
)
eval_callback = EvalCallback(env,
    callback_after_eval=stop_callback,
    eval_freq=10000,
    best_model_save_path=save_path,
    verbose=1
)
logging_callback = LoggingCallback(verbose=1)
# wandb_callback = WandbCallback(verbose=2, log="all", gradient_save_freq=100)

callbacks = CallbackList([logging_callback, eval_callback])

model = PPO("MultiInputPolicy", env, verbose=1, tensorboard_log=log_path)
model.learn(timesteps, callback=callbacks)

# wandb.finish()