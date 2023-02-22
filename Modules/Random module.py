from random import random,randint,choice,shuffle
# import random : This way of importing is preferable since devs reading this code won't be able
# to make out which functions were used

print(random())
print(randint(1, 10))
print(choice([1, 2, 3, 4, 5, 6]))
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
shuffle(my_list)
print(my_list)
