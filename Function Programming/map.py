my_list = [1, 2, 3, 4, 5, 6]
usernames = ('kaustubh', 'eshani', 'rambo', 'utsav')


def multiply_by2(item):
    """Returns the list with elements multiplied by 2"""
    return item * 2


def convert_upper(item):
    """Converts iterables to upper case"""
    return item.upper()


print(list(map(multiply_by2, my_list)))  # map function does not modify the original list
print(my_list)  # my_list in intact and not affected by above function call

print(tuple(map(convert_upper, usernames)))
print(usernames)
