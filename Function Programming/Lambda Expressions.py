# Lambda Expressions are one time anonymous functions that does not have any name, and it does not need to run more
# than once. Lambda Expressions are used only once and not stored like functions
# Once the function is executed it is no longer stored in memory, hence making it a one time use
from functools import reduce

my_list = [1, 2, 3, 4, 5, 6]
usernames = ('kaustubh', 'eshani', 'rambo', 'utsav')


def multiply_by2(item):
    """Returns the list with elements multiplied by 2"""
    return item * 2


def only_odd(items):
    return items % 2 == 1


print(list(map(multiply_by2, my_list)))

print(list(map(lambda item: item * 2, my_list)))  # lambda expressions are one time functions, the above code was
# implemented in a line

print(list(filter(only_odd, my_list)))  # Filters odd nums using function
print('Odd Nums', list(filter(lambda items: items % 2 == 1, my_list)))  # Filters odd numbers using Lambda expression

print(reduce(lambda acc, item: acc + item, my_list, 0))  # Reduce function using lambda expressions

print(list(map(lambda items: items.upper(), usernames)))  # Convert to upper case using lambda functions
