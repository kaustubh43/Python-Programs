from collections import Counter, defaultdict, OrderedDict

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d2 == d1)

# Ordered Dictionary creates an ordered dictionary
# In a regular dictionary order of insertion does not matter since dictionary
# is an unordered collection of key value pairs


# Recently, the Python has made Dictionaries ordered by
# default! So unless you need to maintain older version
# of Python (older than 3.7), you no longer need to use ordered
# dict, you can just use regular dictionaries!
