my_file = open('text.txt')

print(my_file.read())
my_file.seek(0)  # Points the cursor to the start of the file
print(my_file.read())
my_file.seek(0)  # Points the cursor to the start of the file
print(my_file.read())