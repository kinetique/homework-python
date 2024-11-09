import random

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}


class Player:
    def __init__(self, players_money=5000):
        self.money = players_money

    def bet(self, amount):
        return amount <= self.money

    def won_money(self, amount):
        self.money += amount


class ChoHan:
    HOUSE_FEE = 40

    def __init__(self):
        self.player = Player()

    def roll_dice(self):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        return die1, die2

    def cho_han_sum(self, die1, die2):
        return 'cho' if (die1 + die2) % 2 == 0 else 'han'


def main():
    pass


if __name__ == '__main__':
    main()
