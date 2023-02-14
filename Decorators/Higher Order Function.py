def greet(func):  # Example of Higher Order Function
    func()


def greet2():  # Another Example of Higher order function
    def func():
        return 5

    return func


print(greet2())