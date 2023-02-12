# Square
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda n: n**2, nums))
print(squares)

# List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda x: x[-1])
print(a)


