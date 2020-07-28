# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 09:27:15 2020

@author: Harsh Anand
"""
import pytesseract

import cv2
            
#pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
    
img = "E:\\Forsk\\Project\\College\\expression\\expression\\a.png"
            

            
text = pytesseract.image_to_string(img)
print("expression is :",text)
text = eval(text)

            # Evaluating Expression
print("Value of expression is :",text)