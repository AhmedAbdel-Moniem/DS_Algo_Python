import qrcode
img = qrcode.make("https://www.facebook.com/Dahab.travel/")
img.save("qr.png", "PNG")