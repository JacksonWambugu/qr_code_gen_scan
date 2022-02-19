import  pyqrcode
import webbrowser
from pyzbar.pyzbar import decode
from PIL import Image
print("you can check the QRcode image from the file 'myCode.png'")
inuser=input("enter the link to the site you want ::  ")
#qr = pyqrcode.create("https://github.com/jaksehsekhja/flashlight-app")
qr=pyqrcode.create(inuser)
qr.png("myCode.png",scale=8)
iu=input("do you want to open the link y/n for yes or no  ::  ")
if(iu=='y'):
    d=decode(Image.open("myCode.png"))
    url=d[0].data.decode("ascii")
    webbrowser.open(url)
else:
    print("have a lovely day ")
