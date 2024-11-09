import random


class Computer:
    def __init__(self):
        self.memory = {
            "0x1150": "RESOLVE",
            "0x1250": "CHICKEN",
            "0x1160": "ADDRESS",
            "0x1260": "DESPITE",
            "0x1180": "REFUGEE",
            "0x1280": "DISPLAY",
            "0x11a0": "PENALTY",
            "0x12a0": "IMPROVE"
        }

        self.password = random.choice(list(self.memory.values()))

    def check_guess(self, guess):
        correct_count = 0
        for i in range(len(self.password)):
            if self.password[i] == guess[i]:
                correct_count += 1
        return correct_count


class Hacker:
    def __init__(self, computer, max_guesses=4):
        self.computer = computer
        self.attempts_left = max_guesses

    def play(self):
        print("Find the password in the computer's memory:")
        for address, word in self.computer.memory.items():
            print(f"{address} {word}")

        while self.attempts_left > 0:
            print(f"Enter a password: ({self.attempts_left} tries remaining)")
            guess = input("> ").upper()

            if guess not in self.computer.memory.values():
                print("Invalid password. Try again.")
                self.attempts_left -= 1
                continue

            correct_count = self.computer.check_guess(guess)
            if correct_count == len(self.computer.password):
                print("A C C E S S   G R A N T E D")
                return
            else:
                print(f"Access Denied ({correct_count}/{len(self.computer.password)} correct)")
                self.attempts_left -= 1

        print("Out of attempts! Access permanently denied.")


def main():
    computer = Computer()
    game = Hacker(computer, max_guesses=4)
    game.play()


if __name__ == '__main__':
    main()
