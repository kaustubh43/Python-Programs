with open('text2.txt') as my_file: # using with statement a file is opened in the block
    print(my_file.readlines())

# The file is closed once the block is executed
# Hence you cannot use my_file here
# print(my_file.readlines()) No can do
