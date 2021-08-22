import random


class Dice:
    def roll(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        result = (dice1, dice2)

        return result


game = Dice()

print(game.roll())
