# This script is a tutorial for PIL package
# From the next youtube URL: https://www.youtube.com/watch?v=6Qs3wObeWwc, https://www.youtube.com/watch?v=dkp4wUhCwR4
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np
import os


def looping_image_dir_change_format(dir_path: str):
    """"Over loop on image dir and changing the format of them from .jpg to .png"""
    for f in os.listdir(dir_path):
        if f.endswith(".jpg"):
            fn, fext = os.path.splitext(f)
            im = Image.open(os.path.join(dir_path, f))
            os.makedirs(f'{dir_path}\PNG', exist_ok=True)
            im.save(f'{dir_path}\PNG\{fn}.png')


def image_prop(image_path: str):
    """"Output properties of image to the user"""
    im = Image.open(image_path)
    print(f'Image size: {im.size}\nImage format: {im.format}\nImage mode: {im.mode}')


def image_crop(image_path: str, coor: tuple):
    """"Output crop of an image set by the user
    @ coor: left, top, right, bottom
    """
    im = Image.open(image_path)
    crop_image = im.copy().crop((coor))
    plt.imshow(crop_image)
    plt.show()


def image_transpose(image_path: str):
    """"Output s of an input image: flipping, rotate, transpose"""
    im = Image.open(image_path)
    plt.figure(figsize=(10, 10))
    transpose_image1 = im.transpose(Image.FLIP_LEFT_RIGHT)
    transpose_image2 = im.transpose(Image.FLIP_TOP_BOTTOM)
    transpose_image3 = im.transpose(Image.ROTATE_90)
    transpose_image4 = im.transpose(Image.ROTATE_180)
    transpose_image5 = im.transpose(Image.ROTATE_270)
    transpose_image6 = im.transpose(Image.TRANSPOSE)
    plt.subplot(3, 2, 1)
    plt.imshow(transpose_image1)
    plt.title("FLIP_LEFT_RIGHT")

    plt.subplot(3, 2, 2)
    plt.imshow(transpose_image2)
    plt.title("FLIP_TOP_BOTTOM")

    plt.subplot(3, 2, 3)
    plt.imshow(transpose_image3)
    plt.title("ROTATE_90")

    plt.subplot(3, 2, 4)
    plt.imshow(transpose_image4)
    plt.title("ROTATE_180")

    plt.subplot(3, 2, 5)
    plt.imshow(transpose_image5)
    plt.title("ROTATE_270")

    plt.subplot(3, 2, 6)
    plt.imshow(transpose_image6)
    plt.title("TRANSPOSE")
    plt.show()


def image_resize(image_path: str, new_size: tuple):
    """"Output transpose of an input image: flipping, rotate, transpose
    @ new_size: width, height
    """
    im = Image.open(image_path)
    plt.figure(figsize=(10, 10))
    resize_image1 = im.resize(new_size, Image.BILINEAR)
    resize_image2 = im.resize(new_size, Image.NEAREST)
    resize_image3 = im.resize(new_size, Image.BOX)
    resize_image4 = im.resize(new_size, Image.HAMMING)
    resize_image5 = im.resize(new_size, Image.BICUBIC)
    resize_image6 = im.resize(new_size, Image.LANCZOS)
    plt.subplot(3, 2, 1)
    plt.imshow(resize_image1)
    plt.title("BILINEAR")

    plt.subplot(3, 2, 2)
    plt.imshow(resize_image2)
    plt.title("NEAREST")

    plt.subplot(3, 2, 3)
    plt.imshow(resize_image3)
    plt.title("BOX")

    plt.subplot(3, 2, 4)
    plt.imshow(resize_image4)
    plt.title("HAMMING")

    plt.subplot(3, 2, 5)
    plt.imshow(resize_image5)
    plt.title("BICUBIC")

    plt.subplot(3, 2, 6)
    plt.imshow(resize_image6)
    plt.title("LANCZOS")
    plt.show()


def image_rotation(image_path: str, angle: float):
    """"Out put rotational of the image set by the user"""
    im = Image.open(image_path)
    image_rotation = im.rotate(angle)
    plt.imshow(image_rotation)
    plt.show()

def text_rectangle_on_image(image_path: str, text:str, rec_coor:tuple):
    """"Writing text and drawing rectangle on
    @ rec_coor: left, top, right, bottom
    """
    im = Image.open(image_path)
    watermark_image = im.copy()

    draw = ImageDraw.Draw(watermark_image, "RGBA") # for opacity option
    font = ImageFont.truetype(font=r'C:\Users\liran\git\Python_pack_automotive\PIL\Image_dir\Font\arial.ttf', size=20)

    draw.text((0,0), text, font=font, fill=(255, 255, 255))
    draw.rectangle(rec_coor, fill=(255, 255, 255, 200), outline="blue")
    plt.imshow(watermark_image)
    plt.show()

def resize_and_paste_on_image(image_path:str, new_size:tuple):
    """"Resize image and paste it on the corner of the original image"""
    im = Image.open(image_path)
    image_resize = im.copy()
    image_resize.thumbnail(new_size)
    copied_image = im.copy()
    copied_image.paste(image_resize, (0, 0))
    plt.imshow(copied_image)
    plt.show()


if __name__ == '__main__':
    dir_path = r"C:\Users\liran\git\Python_pack_automotive\PIL\Image_dir"
    image_path = r"C:\Users\liran\git\Python_pack_automotive\PIL\Image_dir\image1.jpg"
    coor = (125, 0, 250, 100)
    new_size = (50, 50)
    angle = 30
    rec_coor = (224, 134, 274,184)
    # looping_image_dir_change_format(dir_path)
    # image_prop(image_path)
    # image_crop(image_path, coor)
    # image_transpose(image_path)
    # image_resize(image_path, new_size)
    # image_rotation(image_path, angle)
    # text_rectangle_on_image(image_path, "Seahorse", rec_coor)
    resize_and_paste_on_image(image_path, new_size)
