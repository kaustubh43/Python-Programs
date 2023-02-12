from functools import reduce
my_list = [1,2, 3, 4, 5, 6, 7]
user_name = ['Kaustubh', 'Eshani', 'Utsav', 'Rambo']


def accumulate(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulate, my_list, 10))  # Reduce gives us one value towards the endm
# It adds up the iterable
print(reduce(accumulate, user_name, '*'))  # It combines like a fibonacci series or summation of n numbers by saving an intermediate output
# Used by advanced programmers