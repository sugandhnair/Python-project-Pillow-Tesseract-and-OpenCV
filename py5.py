import zipfile
import PIL

from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFont, ImageDraw

filename = 'readonly/small_img.zip'
#filename = 'readonly/images.zip'

with zipfile.ZipFile(filename,'r') as myzip:
    myzip.printdir()
    myzip.extractall()
    print("Done")
    
# loading the face detection classifier
def extractor(extracted_file,keyword_search):
    filename = extracted_file
    keyword_search = keyword_search
    face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')
    text = pytesseract.image_to_string(filename)
    if(keyword_search in text):
        image = Image.open(filename)
        cv_image = cv.imread(filename)
        faces = face_cascade.detectMultiScale(cv_image,1.72)
        drawing=ImageDraw.Draw(image)
        image_width = 500
        image_height = 200
        drawingboard = PIL.Image.new(image.mode,(image_width,image_height))
        row = 0
        col = 0
        i=1
        for x,y,w,h in faces:
            drawing.rectangle((x,y,x+w,y+h), outline="white")
            cropped = image.crop((x,y,x+w,y+h))
            
            if(row>=500):
                row = 0
                col = 100
                i=0
            drawingboard.paste(cropped,(row,col))
            row  = 100*i
            res = 1
            i+=1
        if(res > 0):
            print('Results found in {} '.format(filename))
            display(drawingboard)
        else:
            print('Result found in {} but no faces were found'.format(filename))
    return

extracted_files = []

for i in range(15):
    zip_filename = 'a-{}.png'.format(i) 
    try:
        temp = Image.open(zip_filename)
        extracted_files.append(zip_filename)
    except:   
        pass
keyword = input('Enter the keyword :')

for extracted_file in extracted_files:
    result = extractor(extracted_file,keyword)
    
print('Process completed , Have a nice day.')