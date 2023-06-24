import os
from PIL import Image


PAGE_NAME = "www.eneba.com/es/collection/juegos-en-oferta"
IM_NAME = PAGE_NAME.replace('/', '-').replace('.', '-') + ".png"

def make_photo():
    try:
        os.remove(IM_NAME)
    except Exception as e:
        print(e)

    # Do the screenshot of the webpage
    os.system("shot-scraper https://" + PAGE_NAME)

    img = Image.open(IM_NAME)

    # Crop the screenshot
    box = (0, 0, 770, 800)
    img2 = img.crop(box)

    # Save the screenshot
    img2.save(IM_NAME)