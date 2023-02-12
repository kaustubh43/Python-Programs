my_list = [1, 2, 3, 4, 5, 6]
usernames = ('kaustubh', 'eshani', 'ramb0', 'Utsav')


def check_odd(item):
    """Checks if the numbers in list are odd"""
    return item % 2 == 1


def check_lower(item):
    """Checks if list elements are lower case"""
    return item.islower()


print(list(filter(check_odd, my_list)))  # Filter functions act on the iterables and return the filtered iterable
print(my_list)                           # Filtered iterable can be less than or equal to the passed iterable/argument.
print(tuple(filter(check_lower, usernames)))  # Hence the name fileter
print(usernames)


