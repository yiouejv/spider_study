#encoding: utf-8

from PIL import Image
from pytesseract import image_to_string

tesseract_cmd = "C:\\Tesseract-OCR\\tesseract.exe"
image = Image.open('C://test1.jpg')
text = image_to_string(image)
print(text)

