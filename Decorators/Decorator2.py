# A decorator is function that wraps another function
# and enhances it
def my_decorator(func):
    def wrap_func():
        print('*********')
        func()
        print('*********')

    return wrap_func


@my_decorator
def hello():
    print('Hello')


@my_decorator  # define decorator functions
def bye():
    print('See you later')


def greet():
    print('How are you')


hello()
bye()

greet2 = my_decorator(greet)  # Without decorators code will look like this
greet2()  # two lines to do the same as decorator

my_decorator(hello)()  # or it would look like this
