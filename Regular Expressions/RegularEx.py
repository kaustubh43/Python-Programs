import re

string = 'search this inside of this text please!'

pattern = re.compile('search')
print('search' in string)

a = re.search('search', string)
print(a.span())  # shows the starting and ending indices
print(a.start())  # shows the starting index
print(a.end())  # shows the ending index
print(a.group())

print('Using Pattern')
b = pattern.search(string)
c = pattern.findall(string)
d = pattern.fullmatch(string)
e = pattern.match(string)
print(c)
print(d)
print(e)

