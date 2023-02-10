class User:
    def __init__(self, email):
        self.email = email

    @staticmethod
    def sign_in(name):
        print(f"User {name} is signed in successfully")

    def attack(self):
        print("Punch the opponent")


class Wizard(User):
    """Subclass derived from parent class"""

    def __init__(self, name, power, email):
        super().__init__(email)  # Or use User.__inti__(self, email)
        self.name = name
        self.power = power
        print('User created')
        self.sign_in(self.name)

    def attack(self):
        User.attack(self)  # Calls attack in parent class
        print(f"Attacking with power {self.power}")


class Elf(User):
    def __init__(self, name, arrows, email):
        super().__init__(email)   # Or use User.__inti__(self, email)
        self.name = name
        self.arrows = arrows
        print('User created')
        self.sign_in(self.name)

    def attack(self):
        User.attack(self)  # Calls attack in parent class
        print(f"Attacking with power {self.arrows} arrows")


def player_attack(char):  # Polymorphism, calls attack method based on the object that is passed
    char.attack()


wizard1 = Wizard('Harry', 'Pitradev sanrakshanam', 'HarryPotter@gmail.com')
player_attack(wizard1)
elf1 = Elf('Dobby', 40, 'Dobby@gmail.com')
player_attack(elf1)
print(f"Email is {wizard1.email}")
print(dir(wizard1))