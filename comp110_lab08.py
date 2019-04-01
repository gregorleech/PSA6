"""
Module: comp110_lab08

Modules with some functions for Lab 08 practice problems.
"""
from cImage import *
import math

def double(oldimage):
    """ 
    Returns a new image that is a copy of
    oldImage, but twice the size.
    """
    oldw = oldimage.getWidth()    
    oldh = oldimage.getHeight()

    newim = EmptyImage(oldw*2,oldh*2)   

    for row in range(newim.getHeight()):
        for col in range(newim.getWidth()):
            originalCol = col//2
            originalRow = row//2
            
            oldpixel = oldimage.getPixel(originalCol, originalRow)

            newim.setPixel(col, row, oldpixel)
        
    return newim
    
def resize(imageFile):
    """ 
    Code to test the double function.
    """
    old_image = FileImage(imageFile)
    image_window = ImageWin("Input Image", old_image.getWidth(), old_image.getHeight())
    old_image.draw(image_window)
    
    double_image = double(old_image)   
    double_image_window = ImageWin("Resized Image", 
        double_image.getWidth(), double_image.getHeight()) 
    double_image.draw(double_image_window)

    
    image_window.exitOnClick()
    double_image_window.exitOnClick()

def halve(oldimage):
    """ 
    Returns a new image that is a copy of
    oldImage, but half the size.
    """

    return oldimage # you will replace this line


def display(img, title):
    """
    Displays the given image in a new window with the given title for the
    window. Return the new window
    """
    img_win = ImageWin(title, img.getWidth(), img.getHeight())
    img.draw(img_win)
    img_win.exitOnClick()
    return img_win


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

def getColorClick(image):
    '''
    This function takes an image, displays it in a window and
    allows the user to click around the image to find out the
    pixel values.  The user clicks in the upper left hand corner
    (smaller than (10,10)) twice to stop (or hits <ctl-c>). 

    Typical output (pixel at 181,318 has red = 141, etc.):

    [(181, 318), (141, 211, 95)]

    '''
    position = [10,10]
    image_win = ImageWin("", image.getWidth(), image.getHeight())
    image.draw(image_win)
    while position[0] >= 10 and position[1] >= 10 : 
        position = image_win.getMouse()
        print([ position, image.getPixel(position[0],position[1])])
    image_win.exitOnClick()

def intensify_pixel(pixel):
    '''
    Returns an absolute color for a pixel.
    
    '''
    max_color_distance = 255 # Why do I use 255 to create the distance threshold for testing?
    dist_threshold = 3 * max_color_distance **2 

    red = pixel.getRed()
    green = pixel.getGreen()
    blue = pixel.getBlue()
    
    # We will be finding the distance from either a 'pure' color (255) or the 'grayer' color closest to where we are
    max_color = 255 #max(red,green,blue)

    # Note that distance requires the square root, but if we are just using
    # the numbers for comparison, no need to calculate the root

    dist_red = (max_color-red)**2 + green**2 + blue**2
    dist_blue = red **2 + green**2 + (max_color-blue)**2
    dist_yellow = (max_color-red)**2 + (max_color-green)**2 + blue**2
    dist_black = red **2 + green**2 + blue**2
    dist_white = (max_color-red)**2 + (max_color-green)**2 + (max_color-blue)**2

    dist_min = min(dist_threshold,dist_red,dist_blue,dist_yellow,dist_black,dist_white)
    #dist_min = min(dist_black,dist_white)

    
    if dist_red is dist_min:
        pixel = Pixel(255,255,255) # check this line!
    elif dist_blue is dist_min:
        pixel = Pixel(0,0,255)
    elif dist_yellow is dist_min:
        pixel = Pixel(255,255,0)
    elif dist_black is dist_min:
        pixel = Pixel(0,0,255) # check this line!
    elif dist_white is dist_min:
        pixel = Pixel(255,255,255)
    #else they are all greater than the threshold, so no change!!
    return pixel




if __name__ == "__main__":
    blues = FileImage("blues.gif")
    intense_blues = pixelMapper(blues,intensifyPixel)
    display(intense_blues,"Intense")
# only uncomment the line below when you are done!
# blues.save("blues_processed.gif")