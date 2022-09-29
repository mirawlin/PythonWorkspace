

class Game:
    rolls = []

    def score(self) -> int:
        score = 0
        roll_number = 0
        for frame in range(10):
            if self.rolls[roll_number] + self.rolls[roll_number+1] == 10:
                score += 10 + self.rolls[roll_number+2]
                roll_number += 2
            else:
                score += self.rolls[roll_number] + self.rolls[roll_number+1]
                roll_number += 2

        return score

    def roll(self, pins: int):
        self.rolls.append(pins)

