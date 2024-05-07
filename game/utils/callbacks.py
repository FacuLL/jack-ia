from stable_baselines3.common.callbacks import BaseCallback

class LoggingCallback(BaseCallback):
    def __init__(self, verbose=0):
        super().__init__(verbose)
        self.results = {
            "win": 0,
            "lose": 0,
            "tie": 0
        }

    def _init_callback(self) -> None:
        super()._init_callback()

    def _on_step(self) -> bool:
        # Logs on every round
        if "result" in self.locals["infos"][0]:
            if self.locals["infos"][0]["result"] in self.results:
                self.results[self.locals["infos"][0]["result"]]+=1
                print(self.results)
        return True
    
    def _on_rollout_start(self) -> None:
        super()._on_rollout_start()
        wins = self.results["win"]
        loses = self.results["lose"]
        ties = self.results["tie"]
        if wins != 0 or loses != 0 or ties != 0:
            self.logger.record("rollout/round_winrate", (wins / (wins + loses + ties) * 100))
        self.resetResults()
    
    def resetResults(self) -> None:
        self.results["win"] = 0
        self.results["lose"] = 0
        self.results["tie"] = 0