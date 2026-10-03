import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import HorizontalBarsDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask


website_link='https://www.wfmt.com/2023/02/25/anna-knight-19-piano'

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(website_link)
qr.make()

img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=HorizontalBarsDrawer(),
    color_mask=RadialGradiantColorMask()
)

img.save('anna_wfmt_qr.png')
