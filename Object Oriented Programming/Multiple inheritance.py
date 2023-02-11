class User:
    @staticmethod
    def sign_in(name):
        print(f"User {name} is signed in successfully")

    def attack(self):
        print("Punch the opponent")


class Wizard(User):
    """Subclass derived from parent class"""

    def __init__(self, name, power):
        self.name = name
        self.power = power
        print('User created')
        self.sign_in(self.name)

    def attack(self):
        print(f"Attacking with power {self.power}")


class Elf(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
        print('User created')
        self.sign_in(self.name)

    def attack(self):
        print(f"Attacking with power {self.arrows} arrows")

    def run(self):
        print(self.name, 'ran really fast')


class Hybrid(Wizard, Elf):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Elf.__init__(self, name, power)
        # super().__init__(name, arrows), cant use super method here
        # super().__init__(name, arrows), cant use super method here


def player_attack(char):  # Polymorphism, calls attack method based on the object that is passed
    char.attack()


player_hybrid = Hybrid('Dumbledore', 'Elder Wand', 45)
player_hybrid.run()
print(player_hybrid.name, 'has', player_hybrid.arrows, 'arrows')
