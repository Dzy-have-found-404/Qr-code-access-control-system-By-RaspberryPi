#！/ usr / bin / env python 
# - * - coding：utf-8 - * - 
""" 
__title__ ='$ Package_name' 
__author__ ='$ USER' 
__mtime__ ='$ DATE' 

"""
from PIL import Image
import zbarlight

file_path = '/home/pi/pywork/menjin/image.jpg'
with open(file_path, 'rb') as image_file:
    image = Image.open(image_file)
    image.load()

codes = zbarlight.scan_codes(['qrcode'], image)
print('QR codes: %s' % codes)