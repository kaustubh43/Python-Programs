from collections import Counter, defaultdict, OrderedDict
di = {
    'a': 1,
    'b': 2
}
print(di['a'])
# print(di['z'])  # This will result into an error since the key doesn't exist

print('Using Default Dictionary')
di2 = defaultdict(int, {'a': 1, 'b': 2})
print(di2['a'])
print(di2['z'])

print('Using Default Dictionary2')
di3 = defaultdict(lambda:'does not exist', {'a': 1, 'b': 2})
print(di3['a'])
print(di3['z'])
