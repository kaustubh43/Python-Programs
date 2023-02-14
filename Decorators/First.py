def hello():
    print('Hello')


greet = hello
del hello
greet()

