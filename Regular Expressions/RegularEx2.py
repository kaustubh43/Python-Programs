import re

string = 'search this inside of this text please!'

pattern = re.compile(r'([a-zA-Z]).(a)')


a = pattern.search(string)


b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(c)
print(d)
print(a.group(2))

