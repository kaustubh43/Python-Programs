from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
# new_img = img.resize((400, 200))  # this method can sometimes ruin the aspect ratio
img.thumbnail((400, 400))  # Instead use this
# new_img.save('astro_thumbnail.jpg')
img.save('astro_thumbnail.jpg')
