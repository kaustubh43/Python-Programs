# Clubbing specific errors into one except block
def div(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'Please enter a number \nError: {err}')


print(div(1, '2'))  # Type Error
print(div(1, 0))  # Zero Division Error
print(div(1, 24))  # No error
