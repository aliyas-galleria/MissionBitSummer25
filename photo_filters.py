from PIL import Image 
from PIL import Image, ImageFilter
from PIL import Image, ImageEnhance

image = Image.open('sample_image.jpg')
image.show()

resized_image = image.resize((100,100))
resized_image.show()

rotated_image = image.rotate(90)
rotated_image.show()

grayscale_image = image.convert('L')
grayscale_image.show()

blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.show()

enhancer = ImageEnhance.Color(image)
enhanced_color_image = enhancer.enhance(1.5)
enhanced_color_image.show()

resized_image.save('resized_image.jpg')
rotated_image.save('rotated_image.jpg')
grayscale_image.save('grayscale_image.jpg')
blurred_image.save('blurred_image.jpg')
enhanced_color_image.save('enhanced_color_image')
