def multiply_by2(li):
    """Returns the list with elements multiplied by 2"""
    new_list = []
    for _ in li:
        new_list.append(_ * 2)
    return new_list

# A pure function returns the same result every single time and doesn't react with the outside world
# Pure functions lead to less buggy code
# Different parts of code doesn't affect or react with each other


print(multiply_by2([1, 2, 3, 4, 5]))
