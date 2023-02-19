# A generator function that yields 1 for first time,
# 2 second time and 3 third time
# Below code is referenced from GFG
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)

x = simpleGeneratorFun()  # x is a generator object
print(next(x))
print(next(x))
print(next(x))
