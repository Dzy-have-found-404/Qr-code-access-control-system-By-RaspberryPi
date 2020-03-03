#！/ usr / bin / env python 
# - * - coding：utf-8 - * - 
""" 
__title__ ='$ Package_name' 
__author__ ='$ USER' 
__mtime__ ='$ DATE' 

"""
import os, signal, subprocess

strfile1 = "qrcode"

def erzeugen():
    text = input ("enter text QRCode: ")
    os.system("qrencode -o " + strfile1 + ".png '" + text + "'")
    print ("QRCode in: " + strfile1 + ".png")

def lesen():
    os.system("sudo raspistill -w 320 -h 240 -o /home/pi/pywork/menjin/image.jpg")
    print ("raspistill finished")
    # zbarcam=subprocess.Popen("zbarcam --raw --nodisplay /dev/video0", stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
    # print u"zbarcam started successfully..."
    # qrcodetext=zbarcam.stdout.readline()
    zbarcam = subprocess.Popen("zbarimg --raw /home/pi/pywork/menjin/image.jpg", stdout=subprocess.PIPE, shell=True,
                               preexec_fn=os.setsid)
    qrcodetext = zbarcam.stdout.readline()
    if qrcodetext != "":
        print (qrcodetext)
    else:
        print ("qrcodetext is empty")

    # os.killpg(zbarcam.pid, signal.SIGTERM)
    print ("zbarcam stopped successfully...")
    return str("QRCode: ")+ str(qrcodetext)
