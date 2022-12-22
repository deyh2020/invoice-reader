try:
    import pytesseract
    import cv2

    from PIL import Image

except:

    raise Exception ("Cannot Import Required Modules.")
    exit()

pytesseract.tesseract_cmd = r'C:\Users\alex\AppData\Local\Programs\Python\Python39\Lib\site-packages\pytesseract'

class Read():

    def __init__(self, file):
        


        if file != None:

            print(pytesseract.image_to_string(Image.open(file)))




            #temp = open(file)
            #print(temp)

        else:

            raise Exception ("File Not Found.")