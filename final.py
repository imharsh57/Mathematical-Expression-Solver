from PIL import Image
from pytesseract import image_to_string
import numpy as np

img=Image.open('a.png')


text = image_to_string(img)

print(eval(text))

