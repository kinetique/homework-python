import random

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}


class Player:
    def __init__(self, players_money=5000):
        self.money = players_money

    def bet(self, amount):
        return amount <= self.money

    def update_money(self, amount):
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

    def one_round(self, bet_amount, players_choice):
        if not self.player.bet(bet_amount):
            return "You don't have enough money for the bet!"

        die1, die2 = self.roll_dice()
        result = self.cho_han_sum(die1, die2)

        print("The dealer lifts the cup to reveal:")
        print(f"{JAPANESE_NUMBERS[die1]} - {JAPANESE_NUMBERS[die2]}")
        print(f"{die1} - {die2}")

        if result == players_choice:
            winnings = bet_amount - self.HOUSE_FEE
            self.player.update_money(winnings)
            print(f"You won {winnings} money! The house collected 40 money fee.")
        else:
            self.player.update_money(-bet_amount)
            print(f"You lost {bet_amount} money! Better luck next time!")

    def start_game(self):
        print("Welcome to Cho-Han game!Let's try your luck!")
        while self.player.money > 0:
            print(f"You have {self.player.money} mon. How much do you bet? (or QUIT)")
            bet = input("> ")
            if bet.lower() == 'quit':
                print("Thank you for playing!")
                break

            try:
                bet_amount = int(bet)
                if bet_amount <= 0:
                    print("You can't bet negative numbers!")
                    continue
            except ValueError:
                print("Please enter a number!")
                continue

            if not self.player.bet(bet_amount):
                print("You don't have enough money for the bet!")
                continue

            print("The dealer swirls the cup and you hear the rattle of dice.")
            print("The dealer slams the cup on the floor, still covering the dice and asks for your bet.")
            print("CHO (even) or HAN (odd)?")
            players_choice = input("> ").strip().lower()
            if players_choice not in ('cho', 'han'):
                print("Please enter either 'cho' or 'han'.")
                continue

            self.one_round(bet_amount, players_choice)
            if self.player.money < 0:
                print("Sorry, you lost all the money. Thanks for playing!")
                break


def main():
    game = ChoHan()
    game.start_game()


if __name__ == '__main__':
    main()
