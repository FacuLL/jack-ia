from stable_baselines3.common.callbacks import BaseCallback

class LoggingCallback(BaseCallback):
    def __init__(self, verbose=0, log_freq=1):
        super().__init__(verbose)
        self.rollout_count = 0
        self.results = {
            "win": 0,
            "lose": 0,
            "tie": 0
        }
        self.log_freq = log_freq

    def _init_callback(self) -> None:
        super()._init_callback()

    def _on_step(self) -> bool:
        # Logs on every round
        if "result" in self.locals["infos"][0]:
            if self.locals["infos"][0]["result"] in self.results:
                self.results[self.locals["infos"][0]["result"]]+=1
        return True
    
    def _on_rollout_start(self) -> None:
        super()._on_rollout_start()
        self.rollout_count += 1
        wins = self.results["win"]
        loses = self.results["lose"]
        ties = self.results["tie"]
        
        if self.rollout_count % self.log_freq == 0:
            if wins + loses != 0:
                self.logger.record("rollout/round_winrate", (wins / (wins + loses) * 100))
                self.logger.record("rollout/round_loserate", (loses / (wins + loses) * 100))
            if wins + loses + ties != 0:
                self.logger.record("rollout/round_tierate", (ties / (wins + loses + ties) * 100))
            self.resetResults()
    
    def resetResults(self) -> None:
        self.results["win"] = 0
        self.results["lose"] = 0
        self.results["tie"] = 0