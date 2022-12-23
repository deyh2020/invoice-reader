import pytesseract
import cv2
import matplotlib.pyplot as plt
import pdf2image
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

filename = 'img/invoice4.pdf'

ext = filename.split('.')[-1]

if ext == "pdf":
    ...

elif ext == "png" or ext == "jpg":
    ...

img = cv2.imread(filename)

try:
    h, w, _ = img.shape

except AttributeError as e:
    print("Unsupported file format: ", e)

boxes = pytesseract.image_to_boxes(img)
print(pytesseract.image_to_string(img))

for b in boxes.splitlines():
    b = b.split()
    cv2.rectangle(img, ((int(b[1]), h - int(b[2]))), ((int(b[3]), h - int(b[4]))), (0, 255, 0), 2)

plt.imshow(img)
plt.show()















