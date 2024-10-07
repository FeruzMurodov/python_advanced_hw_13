from logging import exception
from random import randint, choice

KARMA = 500


def one_day():
    daily_karma = randint(1, 7)
    if randint(1, 10) == 5:
        exception_ = choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()])
        raise exception_
    return daily_karma


class KillError(Exception):
    def __init__(self):
        super().__init__("Murder. You are dead!")


class DrunkError(Exception):
    def __init__(self):
        super().__init__("Drunkenness. Fight drunkenness!")


class CarCrashError(Exception):
    def __init__(self):
        super().__init__("You've had an accident. You should watch the road!")


class GluttonyError(Exception):
    def __init__(self):
        super().__init__("You've overeaten. You should cut down on your portions!")


class DepressionError(Exception):
    def __init__(self):
        super().__init__("You are overcome by melancholy. Despondency is a sin!")


if __name__ == '__main__':
    current_karma = 0
    with open('karma.log', 'w', encoding='utf-8') as f_logger:
        while current_karma < KARMA:
            try:
                current_karma += one_day()
            except Exception as e:
                print(f"Unfortunately you have caught an error! {e}")
                f_logger.write(f'{e}\n')
    print(f'You have reached KARMA {current_karma}')
