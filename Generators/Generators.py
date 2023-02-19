# Generator example

def generator_func(num):
    for i in range(num):
        yield i * 2


for item in generator_func(100):
    print(item)

# Instead of creating a list and consume memory
# We printed those numbers in console above

g = generator_func(1000)
print(next(g))
print(next(g))