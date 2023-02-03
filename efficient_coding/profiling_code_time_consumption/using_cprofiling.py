from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
import cProfile
import pstats

#  https://www.youtube.com/watch?v=m_a0fN48Alw&ab_channel=mCoding


def image_enhancment(image_path: str, enhancement_rate: float):
    """Enhancement of image"""

    plt.figure(figsize=(10, 10))
    im = Image.open(image_path)
    image_color_enhan = im.copy()
    image_enhan1 = ImageEnhance.Color(image_color_enhan).enhance(enhancement_rate)  # 1.0 is default value
    image_enhan2 = ImageEnhance.Contrast(image_color_enhan).enhance(enhancement_rate)  # 1.0 is default value
    image_enhan3 = ImageEnhance.Brightness(image_color_enhan).enhance(enhancement_rate)  # 1.0 is default value
    image_enhan4 = ImageEnhance.Sharpness(image_color_enhan).enhance(enhancement_rate)  # 1.0 is default value
    plt.subplot(2, 2, 1)
    plt.imshow(image_enhan1)
    plt.title("Color")
    plt.subplot(2, 2, 2)
    plt.imshow(image_enhan2)
    plt.title("Contrast")
    plt.subplot(2, 2, 3)
    plt.imshow(image_enhan3)
    plt.title("Brightness")
    plt.subplot(2, 2, 4)
    plt.imshow(image_enhan4)
    plt.title("Sharpness")
    plt.show()


if __name__ == '__main__':
    with cProfile.Profile() as pr:
        image_enhancment(r'/PIL/Image_dir/image1.jpg', 2)

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats() # visual the statistc in run window
    stats.dump_stats(filename='needs_profiling.prof')  # and then run in the command line snakeviz
    # ./needs_profiling.prof
