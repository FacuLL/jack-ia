import os
from models.enviroment import Enviroment
from models.player import Player
from models.dealer import Dealer
from stable_baselines3 import A2C
from stable_baselines3.common.callbacks import EvalCallback, StopTrainingOnNoModelImprovement

log_path = os.path.join("Logs")
save_path = os.path.join("RL_Models", "A2C")

mazos = 8
env = Enviroment(mazos, Player(), Dealer())

stop_callback = StopTrainingOnNoModelImprovement(
    max_no_improvement_evals=100000,
    min_evals=2000000,
    verbose=1
)
eval_callback = EvalCallback(env,
    callback_after_eval=stop_callback,
    eval_freq=10000,
    best_model_save_path=save_path,
    verbose=1
)

model = A2C("MultiInputPolicy", env, verbose=1, tensorboard_log=log_path)
model.learn(2000000, callback=eval_callback)