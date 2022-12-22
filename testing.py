import cv2
import pytesseract

img = cv2.imread('basic-invoice-template.png')

text = pytesseract.image_to_string(img)

print(text)
