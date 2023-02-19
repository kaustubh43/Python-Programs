# Generators
>Generators allow us to generate a sequence of values over time
>
> Generator is a function
> 
> range is an example of Generators
> 
> A generator is an iterable but an iterable like a list  is not a generator 
> 
> 
### Yield Keyword
> Yield keyword pauses the function and iterates if next() is used
```  
# Generator example

def generator_func(num):
    for i in range(num):
        yield i * 2


for item in generator_func(100):
    print(item)

# Instead of creating a list and consume memory
# We printed those numbers in console above

g = generator_func(1000) # g is generator object
print(next(g))
print(next(g))
```

 ### [Link for GFG generators](https://www.geeksforgeeks.org/generators-in-python/).
 ### [Link for  generators](https://www.programiz.com/python-programming/generator).