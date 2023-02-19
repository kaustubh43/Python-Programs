# Raise specific errors
while True:
    try:
        age = int(
            input('What is your age '))  # User can enter anything, but basically we want user to enter a positive
        # number
        print('Your age is ', age)
        var = 10 / age
        # break statement can be put here as well
    except ValueError:  # Can add specific Error catching statements
        print('Please enter a valid numeral value')
    except ZeroDivisionError:
        print('Please enter age higher than zero')
    else:
        print('Thank you for your inputs')
        break
