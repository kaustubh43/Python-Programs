from sys import argv
from os import listdir, path, mkdir
from PIL import Image
# This script has to be run from the CLI to convert JPG to PNG
# two arguments from CLI: Firsts one is the source directory, Second on is target directory

x = argv[1]
y = argv[2]

source_files = listdir(f'./{x}')
clean_names = [k.split('.')[0] for k in source_files]
print(clean_names)

if not path.exists(f'./{y}'):
    print('Making a new Directory')
    mkdir(f'./{y}')

for k in clean_names:
    img = Image.open(f'./{x}/{k}.jpg')
    img.save(f'./{y}/{k}.png')

print('Images Saved Successfully')


