from pytesseract import image_to_string 
import Image
import sys

print (image_to_string(Image.open(sys.argv[1]), config='outputbase digits'))