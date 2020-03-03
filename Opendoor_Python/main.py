#！/ usr / bin / env python 
# - * - coding：utf-8 - * - 
""" 
__title__ ='$ Package_name' 
__author__ ='$ USER' 
__mtime__ ='$ DATE' 

"""
#import sys
#sys.path.append(r"F:\源\Raspberry_pi_project\menjin\Opendoor_Python\qrcode\Desktop\python")
import qrcode

while (True):
    print (u"1: qrcode create")
    print (u"2: qrcode identify")
    print (u"3: exit")
    select=int(input(str("please choose: ")))
    if select == 1:
        qrcode.erzeugen()
    elif select == 2:
        result=qrcode.lesen().strip()
        print (result)
    elif select == 3:
        print (str("programme completed..."))
        break

