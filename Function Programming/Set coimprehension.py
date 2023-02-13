# List, Set, Dictionary Comprehensions

# Usual Way
my_set = set({})
for char in 'Hello':
    my_set.add(char)
print(my_set)

# Using list comprehension
my_set2 = {x for x in 'Hello'}
print(my_set2)


# Making a list of nums from 0 to 10
nums = {x for x in range(1, 10)}
print(nums)
# Making a list of nums but multiple each element by 2
nums2 = {x * 2 for x in range(1, 10)}
print(nums2)
# Making a list with power of 2
nums3 ={x**2 for x in range(1,10)}
print(nums3)
# Making a list of power 2 but adding only even elements
nums4 = {x**2 for x in range(1, 10) if x % 2 == 0}
print(nums4)


