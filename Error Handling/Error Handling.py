# error handling
while True:
    try:
        age = int(
            input('What is your age '))  # User can enter anything, but basically we want user to enter a positive number
        print('Your age is ', age)
        # break
    except:
        print('Please enter a valid input')
    else:
        print('Thank you for your inputs')
        break
