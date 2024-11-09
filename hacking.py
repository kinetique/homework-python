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
    pass


def main():
    pass


if __name__ == '__main__':
    main()
