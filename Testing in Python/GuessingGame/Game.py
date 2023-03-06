from random import randint


def run_guess(guess, answer):
    try:
        if 0 < guess < 11:
            if guess == answer:
                print('Bravo You have guessed correctly')
                return True
        else:
            print('I said a number between 1 to 10')
            return False
    except TypeError as err:
        print('please enter a number')
        return err


if __name__ == '__main__':
    rand_num = randint(1, 11)
    while True:
        x = int(input('Enter your Guess 1~10: '))
        if run_guess(x, rand_num):
            break


print('Exiting...')
