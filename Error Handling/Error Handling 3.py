# To print meaningful error prompts using 'as' keyword
def summation(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:  # To print meaningful output or prompts to users if want to catch all errors
        print(f'Please enter a number \nError: {err}')


print(summation('1', 2))
