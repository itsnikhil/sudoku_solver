import cv2
import numpy as np
from PIL import Image
from pytesseract import image_to_string 

img = cv2.imread("/home/nikhil/Downloads/sudoku.png", 0)
ret, thresh = cv2.threshold(img, 10, 255, cv2.THRESH_OTSU)

print "Threshold selected : ", ret
cv2.imwrite("./output.png", thresh)
print image_to_string(Image.open("./output.png"))