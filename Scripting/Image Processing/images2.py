from PIL import Image, ImageFilter

img = Image.open('./Pokemon/pikachu.jpg')
filtered_img = img.convert('L')
filtered_img.save('grayscale.png', 'png')
crooked = filtered_img.rotate(180)
# crooked.save('grayscale90.png', 'png')
resize = crooked.resize((300, 300))
resize.save('grayscale90_resized.png', 'png')

box = 100, 100, 400, 400
crop = filtered_img.crop(box)
crop.save('filtered_crop.png', 'png')
