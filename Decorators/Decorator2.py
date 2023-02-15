# A decorator is function that wraps another function
# and enhances it
def my_decorator(func):
    def wrap_func(*args, **kwargs):  # args and kwargs helps us pass as many parameters
        print('*********')
        func(*args, **kwargs)
        print('*********')

    return wrap_func


@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)


@my_decorator  # define decorator functions
def bye():
    print('See you later')


def greet():
    print('How are you')


hello('Ola Amigos', '👷')

# equivalent of decorator
a = my_decorator(hello)
a('Ola Amigos')
