class Factorial:
    cache = {}

    def __init__(self, n):
        self.n = n

    def factorial(self, n):
        if n in self.cache:
            return self.cache[n]

        if n < 1:
            return 1

        result = n * self.factorial(n-1)
        self.cache[n] = result
        return result


def main():
    n1 = Factorial(5)

    print(n1.factorial(5))
    print(n1.factorial(3))


if __name__ == '__main__':
    main()
