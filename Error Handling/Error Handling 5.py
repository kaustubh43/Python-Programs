# Finally block
count = 0
while True:
    try:
        age = int(
            input('What is your age '))
        print('Your age is ', age)
        var = 10 / age
    except ValueError:
        print('Please enter a valid numeral value')
        count += 1
    except ZeroDivisionError:
        print('Please enter age higher than zero')
        count += 1
    else:
        print('Thank you for your inputs')
        count += 1
        break
    finally:
        print(f'Trial Number {count} tries')

print(count)
