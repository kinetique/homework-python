class Player:
    def __init__(self, players_money=5000):
        self.money = players_money

    def bet(self, amount):
        return amount <= self.money

    def won_money(self, amount):
        self.money += amount


class ChoHan:
    pass


def main():
    pass


if __name__ == '__main__':
    main()
