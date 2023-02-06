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


player1 = PlayerCharacter('Rambo', 24)
print('Object :', player1)
print(f'Player name is {player1.name}')
player1.run(50)
