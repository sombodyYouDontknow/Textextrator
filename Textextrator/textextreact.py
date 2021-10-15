
from PIL import Image
import pytesseract

image = input("enter the image ")

text = pytesseract.image_to_string(Image.open(image))

with open('extract.txt','w') as f :
	f.write(text)

