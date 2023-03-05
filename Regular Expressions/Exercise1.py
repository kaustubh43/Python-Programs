# Password Checker
# Requirements:
# Should have at least 8 characters
# Letters numbers and @#$%

import maskpass
import re
pattern = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[@#$%]).{8,}$")

while True:
    password = maskpass.askpass(prompt="Password:", mask="*")
    a = pattern.fullmatch(password)
    if a:
        print('Your password has been registered')
        break
    else:
        print('Enter a valid password')

print(password)

input('Press any key to exit')

