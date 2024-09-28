import qrcode
import qrcode.constants
import qrcode.image.svg

## Simple
img = qrcode.make("Basic QR Code")
img.save("qrcode.png")

## Advanced
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data("https://www.netflix.com")
qr.make(fit=True)

img = qr.make_image(fill_color=(74, 118, 82), back_color="white")
img = qr.make_image(fill_color=("white"), back_color="black")
img.save("advanced.png")

## Web Version
factory = qrcode.image.svg.SvgPathImage
svg_image = qrcode.make("https://www.youtube.com", image_factory=factory)
svg_image.save("custom.svg")
