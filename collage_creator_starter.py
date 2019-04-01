"""
Module: comp110_psa6

Module with functions for PSA #6 of COMP 110 (Fall 2018).

Authors:
1) Name - USD Email Address
2) Name - USD Email Address
"""

from cImage import *
import math

# TODO: implement the shrink function.

# TODO: implement the get_shrink_factor function.

# TODO: implement your unique pixel filter function.

# TODO: implement your mirror function.

# TODO: implement any other filters you need for your collage.


def create_collage():
    """
    Program to ask the user for an image and desired collage width/height and
    create a 3x2 Andy Worhol style collage using at least 6 unique filters.
    """

    # TODO: implement this function
    print("This function has not been implemented.")


"""
Do NOT modify anything below this point.

The code below mostly comes from your textbook. You may use it to help you
with the functions you have to write. You may also use any of the filters
given below when making your collage. Just don't modify anything below this
point.
"""

def display(img, title):
    """
    Displays the given image in a new window with the given title for the
    window. Return the new window
    """
    img_win = ImageWin(title, img.getWidth(), img.getHeight())
    img.draw(img_win)
    img_win.exitOnClick()
    return img_win


def negativePixel(oldPixel):
    """
    Returns a pixel that is a "negative" version of the given pixel.

    This function is to be used with the pixelMapper function.
    """
    newred = 255 - oldPixel.getRed()
    newgreen = 255 - oldPixel.getGreen()
    newblue = 255 - oldPixel.getBlue()
    newPixel = Pixel(newred, newgreen, newblue)
    return newPixel

def grayPixel(oldpixel):
    """
    Returns a pixel that is the grayscale version of the given pixel.

    This function is to be used with the pixelMapper function.
    """
    intensitySum = oldpixel.getRed() + oldpixel.getGreen() + oldpixel.getBlue()
    avgRGB = intensitySum // 3

    newPixel = Pixel(avgRGB, avgRGB, avgRGB)
    return newPixel


def pixelMapper(oldimage, rgbFunction):
    """
    Creates a new image that is the same as the given image (oldImage) but
    with the rgbFunction applied to every pixel.

    """

    width = oldimage.getWidth()
    height = oldimage.getHeight()
    newim = EmptyImage(width,height)

    for row in range(height):
        for col in range(width):
            originalPixel = oldimage.getPixel(col, row)
            newPixel = rgbFunction(originalPixel)
            newim.setPixel(col, row, newPixel)

    return newim



def verticalFlip(oldimage):
    """
    Creates a new image that is the same as the original, except flipped
    across the vertical axis.

    You may use this code as a template for your mirror function.
    """
    oldw = oldimage.getWidth()
    oldh = oldimage.getHeight()

    newim = EmptyImage(oldw, oldh)

    maxp = oldw - 1
    for row in range(oldh):
        for col in range(oldw):

            oldpixel = oldimage.getPixel(maxp-col, row)

            newim.setPixel(col,row,oldpixel)

    return newim




if __name__ == "__main__":
    create_collage()
