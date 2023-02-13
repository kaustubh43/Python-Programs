some_list = ['a', 'f', 'c', 'd', 'e', 'f', 'n', 'n']

dupli = list(set([x for x in some_list if some_list.count(x) > 1]))
print(dupli)
