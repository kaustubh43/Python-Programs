# Program to Translate a file and its contents to Japanese
file_name = input('Enter the file name that you want to trasnslate: ')
final_file = input('Enter the target file name: ')

try:
    with open(file_name, mode='r') as f1:
        text = f1.read()
except FileNotFoundError as err:
    print('File is not found')
except IOError as err:
    print(err)

try:
    with open(final_file, mode='w') as f2:
        f2.write(text)
except FileNotFoundError as err:
    print('File not found')
except IOError as err:
    print('IO Error')



