# Example to demonstrate generators
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(99999999):   # The Generator here does not store the list hence this function is faster than
        # long_time2
        var = i * 5


@performance
def long_time2():
    for i in list(range(99999999)):  # The list function creates a list in memory and for loop iterates over that
        # list in memory
        var = i * 5


long_time()
long_time2()
