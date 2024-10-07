class ScoreLimitExceededError(Exception):
    pass


class GameScore:
    def __init__(self, score=0):
        if not score < 0:
            self.score = score

    def add_score(self, score):
        if self.score + score > 1000:
            raise ScoreLimitExceededError
        else:
            self.score += score

    def subtract_score(self, score):
        if self.score - score < 0:
            raise ValueError(f"Score can not be negative. Current score {self.score}\n"
                             f"You trying to subtract {score}")
        else:
            self.score -= score


if __name__ == '__main__':
    try:
        game1 = GameScore()
        print(game1.score)
        game1.add_score(900)
        print(game1.score)
        game1.add_score(101)
        print(game1.score)
        game1.subtract_score(777)
        print(game1.score)
        game1.subtract_score(224)
        print(game1.score)
    except ScoreLimitExceededError as e:
        print("You can not add score more than 1000 in total.")
    except ValueError as ev:
        print('You can not subtract the score greater than existing score.')
