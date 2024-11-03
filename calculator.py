class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2


if __name__ == "__main__":
    while True:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            mode = input("Enter mode (+, -, *, /): ")

            if mode == "+":
                result = Calculator(num1, num2).add()
                print(result)
            elif mode == "-":
                result = Calculator(num1, num2).subtract()
                print(result)
            elif mode == "*":
                result = Calculator(num1, num2).multiply()
                print(result)
            elif mode == "/":
                result = Calculator(num1, num2).divide()
                print(result)
        except ValueError:
            print("Please enter a number")
            continue

        program_use = input("Do you want to continue? (y/n): ")
        if program_use != "y":
            print("Thank you!")
            break
