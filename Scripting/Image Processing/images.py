from PIL import Image, ImageFilter

img = Image.open('./Pokemon/pikachu.jpg')

# print(img)
# print(img.format)
# print(img.size)
# print(img.mode)
# print(dir(img)) # more info can be found in documentation

# Blurring an image
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blur.png', 'png')

# Smoothening an image
filtered_img2 = img.filter(ImageFilter.SMOOTH)
filtered_img2.save('smooth.png', 'png')

# Sharpening an image
filtered_img3 = img.filter(ImageFilter.SHARPEN)
filtered_img3.save('sharpen.png', 'png')

# note : PNG supports the filters used above. If jpeg is used then it will give an error

filtered_img4 = img.convert('L')
filtered_img4.save('./Pokemon/grayscale.png', 'png')