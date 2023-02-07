class PlayerCharacter:
    # class object attribute, it is a static attribute which is shared by objetcs
    membership = True

    def __init__(self, name, age):  # constructor method
        if PlayerCharacter.membership:  # You can use self.membership as well
            self.name = name
            self.age = age

    def run(self, distance):  # run the character
        print(f'{self.name} has run {distance} meters')
        return None

    @classmethod
    def adding(cls, num1, num2):
        return num1 + num2
    # class methods can be called without instantiating the class

    @classmethod
    def creating_object(cls, num1, num2):
        return cls('DefaultName', num1 + num2)

    @staticmethod
    # static method has no relation with the class, it's attributes and it's methods
    def mul(num1, num2):
        return num1 * num2


player1 = PlayerCharacter('Rambo', 24)
print('Object :', player1)
print(f'Player name is {player1.name}')
player1.run(50)

# calling class methods with reference to an object
print('calling Class method with ref to object', player1.adding(2, 5))
# calling class methods with reference to class
print('calling Class method with reference to class', PlayerCharacter.adding(5, 6))

# creating an object thorugh a classmethod
player_new = PlayerCharacter.creating_object(5, 6)
print(f'Player name is {player_new.name} and his age is {player_new.age}')

# calling staticmethod with reference to object
print(player_new.mul(5, 6))
# calling staticmethod with reference to class
print(PlayerCharacter.mul(6, 10))
