# Fibonacci Series using Generators

def fib(number):  # This function uses generators
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib(100):
    print(x)


def fib2(num):  # this is traditional method using lists which consumes a lot more memory than usual
    a = 0
    b = 1
    result = list()
    for i in range(num):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result


print(fib2(100))


def fib3(limit):  # This function was referenced from GFG
    a, b = 0, 1
    while a < limit:
        a, b = b, a + b


print('GFG code')
x = fib(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

print('This is using for loops')
y = fib(5)
for i in y:
    print(i)
