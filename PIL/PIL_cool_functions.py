# This script is a tutorial for PIL package
# From the next youtube URL: https://www.youtube.com/watch?v=6Qs3wObeWwc, https://www.youtube.com/watch?v=dkp4wUhCwR4
from PIL import Image
import os


def looping_image_dir_change_format(dir_path:str):
    """"Over loop on image dir and changing the format of them from .jpg to .png"""
    for f in os.listdir(dir_path):
        if f.endswith(".jpg"):
            fn, fext = os.path.splitext(f)
            im = Image.open(os.path.join(dir_path, f))
            os.makedirs(f'{dir_path}\PNG', exist_ok=True)
            im.save(f'{dir_path}\PNG\{fn}.png')

if __name__ == '__main__':
    dir_path = r"C:\Users\liran\git\Python_pack_automotive\PIL\Image_dir"
    looping_image_dir_change_format(dir_path)


