import qrcode
from PIL import Image


def generate_qrCode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,

    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimgae.png")
    img1 = Image.open("qrimgae.png")
    img1.show()


generate_qrCode(input("enter data for QRCode:"))
