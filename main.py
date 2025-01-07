import qrcode
import pyqrcode
import png
from pyqrcode import QRCode
from PIL import Image

# qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
# qr.add_data("https://github.com/c0d3h01")
# qr.make(fit=True)
# img = qr.make_image(fill_color="red", back_color="black")
# img.save("c0d3h01-GitHub.png")

link = "https://github.com/c0d3h01"
url = pyqrcode.create(link)
url.svg("myQR.svg", scale=8) # SVG formmat QR-code
url.png("myQR.png", scale=6) # PNG format QR-code