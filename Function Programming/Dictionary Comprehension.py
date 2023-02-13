simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
my_dict = {key: value**2 for key, value in simple_dict.items()}
print(my_dict)

my_dict2 = {key: value**2 for key, value in simple_dict.items() if value % 2 == 0} #Stores only the odd values of keys
print(my_dict2)

my_dict3 = {num: num * 2 for num in [1, 2, 3, 4, 5]}
print(my_dict3)
