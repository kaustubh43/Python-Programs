# Email Validation using Python
import re

pattern = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
string = input('Enter your email ID: ')

a = pattern.search(string)

if a:
    print('Your email ID has been successfully registered')
else:
    print('You have entered an invalid email ID')
