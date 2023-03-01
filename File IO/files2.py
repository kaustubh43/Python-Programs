my_file = open('text2.txt')

print(my_file.readline())  # This function returns one line from a file
print(my_file.readline())
print(my_file.readline())

my_file.seek(0)

print(my_file.readlines())  # This function returns list of lines contained in a file

my_file.close()  # Need to close a file once you're done using it
# To avoid this refer next file: files3.py