# Error Handling Notes

> An error that crashes our program is called an exception
> 
> Python interpreter raises an exception when an error is encountered
> 
> Error Handling allows us to keep the program running even if errors are encountered
### Built-in Exceptions

 ###### [Link for built-in exceptions](https://docs.python.org/3/library/exceptions.html).

#### Handling errors
```
# error handling
while True:
    try:
        age = int(
            input('What is your age '))  # User can enter anything, but basically we want user to enter a positive
        # number
        print('Your age is ', age)
        var = 10 / age # To Demonstrate ZeroDivError
    except ValueError:  # Can add specific Error catching statements
        print('Please enter a valid numeral value')
    except ZeroDivisionError:
        print('Please enter age higher than zero')
    else:
        print('Thank you for your inputs')
        break
```

##### Catch all errors and display the error message: Use the 'as' keyword. Refer the code below
```
def summation(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:  # To print meaningful output or prompts to users if want to catch all errors
        print(f'Please enter a number \nError: {err}')


print(summation('1', 2))
```

##### Catch specific errors in one except block and display it to the user
```
def div(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'Please enter a number \nError: {err}')


print(div(1, '2'))  # Type Error 
print(div(1, 0))  # Zero Division Error
print(div(1, 24))  # No error
```
#### Finally block
>FinallyThe finally block will be executed no matter if the try block raises an error or not.
>
>This can be useful to close objects and clean up resources. block will be executed if try block 
> 
> Also we can use to lockout a user if he tries to enter the wrong password too many times
```
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
        print(f'Trial number: {count}')
        
print(count)
```

#### Raise Keyword
> The raise keyword is used to raise an exception
> You can define what kind of error to raise and the text to print to the user
```
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")

```