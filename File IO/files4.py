with open('text3.txt', mode='a') as my_file:
    text = my_file.write(' Aloha Kaustubh welcome to Hawaii')
    print(text)

# r+ mode: read write mode starts the cursor at 0 and will overwrite anything if it clashes
# a mode: append mode appends new data to the end of the file
# w mode: write mode resets the contents of the file and starts writing

with open('app/sad.txt', mode='w') as mf:
    text = mf.write(':( this is a sad emoji')
    print(text)