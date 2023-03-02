from translate import Translator
# Program to Translate a file and its contents to Japanese
file_name = input('Enter the file name that you want to translate: ')
final_file = input('Enter the target file name: ')

# Translation stuff
japanese = Translator(to_lang="ja")

# Opening an existing file
try:
    with open(file_name, mode='r') as f1:
        text = f1.read()  # Save read contents into this variable
        with open(final_file, mode='a', encoding="utf-8") as f2:
            trans_japan = japanese.translate(text)
            f2.write(trans_japan)  # Write the translated into a new file
            print('Write Operation completed')
except FileNotFoundError as err:
    print('File is not found')
except IOError as err:
    print(err)




