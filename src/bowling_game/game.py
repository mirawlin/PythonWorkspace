

class Game:
    total_score = 0

    def score(self) -> int:
        return self.total_score

    def roll(self, pins: int):
        self.total_score += pins

