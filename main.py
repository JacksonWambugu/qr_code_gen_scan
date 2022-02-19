import  pyqrcode
import webbrowser
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("https://github.com/jaksehsekhja/flashlight-app")
qr.png("myCode.png",scale=8)

d=decode(Image.open("myCode.png"))
url=d[0].data.decode("ascii")
webbrowser.open(url)
