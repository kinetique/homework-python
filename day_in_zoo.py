class Zookeeper:
    def __init__(self, name):
        self.name = name

    def clean_enclosure(self, enclosure):
        if enclosure.is_clean:
            print(f"The '{enclosure.name}' enclosure is clean.")
        else:
            enclosure.is_clean = True
            print(f"{self.name} just cleaned an enclosure:'{enclosure.name}'")

    def feed_animal(self, animal):
        if animal.is_hungry:
            animal.is_hungry = False
            animal.is_happy = True
            print(f"{self.name} just fed an animal: {animal.name}.")
        else:
            print(f"An animal: {animal.name} is not hungry.")


class Enclosure:
    def __init__(self, name):
        self.name = name
        self.is_clean = False
        self.is_open = False
        self.animals = []

    def open_enclosure(self):
        if self.is_open:
            print(f"The {self.name} is already open.")
        else:
            self.is_open = True
            print(f"The {self.name} is now open.")

    def close_enclosure(self):
        if self.is_open:
            self.is_open = False
            print(f"The {self.name} is now closed.")
        else:
            print(f"The {self.name} is not open.")

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"An animal: {animal.name} is added to the enclosure.")

    def status(self):
        clean_status = "clean" if self.is_clean else "dirty"
        open_status = "open" if self.is_open else "closed"
        print(f"The {self.name} status is: {clean_status}, {open_status}")
        for animal in self.animals:
            animal.status()


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_hungry = True
        self.is_happy = False

    def status(self):
        happiness_status = "happy" if self.is_happy else "sad"
        hungry_status = "hungry" if self.is_hungry else "not hungry"
        print(f"The {self.name} status is: {happiness_status}, {hungry_status}")


class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)


class Bear(Animal):
    def __init__(self, name):
        super().__init__(name)


class Racoon(Animal):
    def __init__(self, name):
        super().__init__(name)


def main():
    zookeeper = Zookeeper("Bob")
    enclosure1 = Enclosure("Lion enclosure")
    enclosure2 = Enclosure("Bear enclosure")
    enclosure3 = Enclosure("Racoon enclosure")

    lion = Lion("Lion")
    bear = Bear("Bear")
    racoon = Racoon("Racoon")

    enclosure1.add_animal(lion)
    enclosure2.add_animal(bear)
    enclosure3.add_animal(racoon)

    enclosure1.open_enclosure()
    enclosure2.open_enclosure()
    enclosure3.open_enclosure()
    enclosure1.status()
    enclosure2.status()
    enclosure3.status()

    zookeeper.clean_enclosure(enclosure1)
    zookeeper.feed_animal(lion)
    zookeeper.clean_enclosure(enclosure2)
    zookeeper.feed_animal(bear)
    zookeeper.clean_enclosure(enclosure3)
    zookeeper.feed_animal(racoon)

    enclosure1.close_enclosure()
    enclosure2.close_enclosure()
    enclosure3.close_enclosure()

    enclosure1.status()
    enclosure2.status()
    enclosure3.status()


if __name__ == "__main__":
    main()