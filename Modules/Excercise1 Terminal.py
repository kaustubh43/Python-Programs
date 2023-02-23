from sys import argv
from random import randint


def guess_num(x1, y1, z1):
    """ Guess the numbers"""
    k = randint(x1, y1)
    if k == z1:
        print("bingo! you've guessed correctly")
        return 1
    else:
        print("Try again next time, Life is a gamble")
    print(f'The Number was {k}')
    return


def take_input():
    """ Takes the input and makes sure that it is within the desire range"""
    while True:
        try:
            guess = input(f'Guess a number between {x}~{y}: ')
            if x <= int(guess) <= y:
                print('all good')
                break
            else:
                print(f'Please enter a value within {x}~{y} ')
        except ValueError:
            print('Please Enter a valid value')
    return int(guess)


x = int(argv[1])
y = int(argv[2])

while True:
    z = take_input()
    if guess_num(x, y, z):
        break
