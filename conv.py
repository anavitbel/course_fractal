from PIL import Image
from PIL import EpsImagePlugin
import os


EpsImagePlugin.gs_windows_binary = r'C:\Program Files\gs\gs9.54.0\bin\gswin64c'


def conv_from_eps_to_img(img_file):
    TARGET_BOUNDS = (1024, 1024)

    pic = Image.open(img_file)
    pic.load(scale=10)

    if pic.mode in ('P', '1'):
        pic = pic.convert("RGB")

    ratio = min(TARGET_BOUNDS[0] / pic.size[0],
                TARGET_BOUNDS[1] / pic.size[1])
    new_size = (int(pic.size[0] * ratio), int(pic.size[1] * ratio))

    pic = pic.resize(new_size, Image.ANTIALIAS)

    os.remove(img_file)
    img_file = '.'.join(img_file.split('.')[:-1])
    img_file += '.png'
    pic.save(img_file)
