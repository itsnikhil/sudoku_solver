import cv2
import numpy as np
from PIL import Image

img = cv2.imread("/home/nikhil/nikhil/Sudoku/sudoku.png", 0)
ret, thresh = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)

print "Threshold selected : ", ret
cv2.imwrite("./output.png", thresh)