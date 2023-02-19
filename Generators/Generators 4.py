# Generators under the hood
# For loop under the hood

def specialForLoop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator) * 2)
        except StopIteration:
            break


specialForLoop([1, 2, 3])
