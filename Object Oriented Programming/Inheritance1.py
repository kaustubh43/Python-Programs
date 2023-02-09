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
        User.attack(self)  # Calls attack in parent class
        print(f"Attacking with power {self.power}")


class Elf(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
        print('User created')
        self.sign_in(self.name)

    def attack(self):
        User.attack(self)  # Calls attack in parent class
        print(f"Attacking with power {self.arrows} arrows")


def player_attack(char):  # Polymorphism, calls attack method based on the object that is passed
    char.attack()


wizard1 = Wizard('Harry', 'Pitradev sanrakshanam')
player_attack(wizard1)
elf1 = Elf('Dobby', 40)
player_attack(elf1)
