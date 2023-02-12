# Two iterables are zipped together using zip()
num1 = [1, 2, 3, 4, 5, 6, 7]
num2 = [8, 9, 10, 11, 12, 13, 14, 15, 16]
user_name = ['Kaustubh', 'Eshani', 'Utsav', 'Rambo']
phone_numbers = [901230124, 99999999, 12837182, 8102381209, 8888888888]
age = [25, 24, 22, 30, 15]


def multiply_by2(item):
    """Returns the list with elements multiplied by 2"""
    return item * 2


def check_odd(item):
    """Checks if the numbers in list are odd"""
    return item % 2 == 1


print(list(zip(num1, num2)))  # Zips the two iterables, first elements of both the iterables are made in to a tuple
print(list(zip(user_name, phone_numbers)))  # All elements are wrapped in a list and return.
# If one iterable is greater than the other, then the extra elements are ignored
print(dict(zip(user_name, phone_numbers)))
print(list(zip(user_name, phone_numbers, age)))  # Zip can contain N number of arguments and can wrap N elements in a tuple
