# hw8pr1.py
# Lab 8
#
# Name: Anirudh Gupta
#

# keep this import line...
from cs5png3 import *

NUM_ITERATIONS = 25  # Number of updates; will be assigned to n
XMIN = -2        # The smallest real coordinate value
XMAX =  1          # The largest real coordinate value
YMIN = -1          # The smallest imaginary coordinate value
YMAX =  1         # The largest imaginary coordinate value


#
# A test function...
#
def test_fun():
    """Algorithmic image creation, one pixel at a time.
       This is a test function: it should create
       an image named test.png in the current directory.
    """
    im = PNGImage(300, 200)  # Creates an image of width 300, height 200

    # Nested loops!
    for r in range(200):     # loops over the rows with runner variable r
        for c in range(300): # loops over the columns with c
            if  c == r:   
                im.plotPoint(c, r, (255, 0, 0))
            #else:
            #    im.plotPoint(c, r, (255, 0, 0))
                
    im.saveFile()

#
# start your Lab 8 functions here:
#


def mult(c, n):
    """Mult multiplies c by the positive integer n,
       using only a loop and addition.
    """
    result = 0
    for i in range(n):
        result += c
    return result

print("mult(105, 3) should be 315 and is", mult(105, 3))

def update(c, n):
    """Update starts with z = 0 and runs z = z**2 + c
       for a total of n times. It returns the final z.
    """
    z = 0
    for i in range(n):
        z = z**2 + c
    return z

def inMSet(c, n):
    """inMSet accepts
            c for the update step of z = z**2+c
            n, the maximum number of times to run that step.
       Then, it returns
            False as soon as abs(z) gets larger than 2.
            True if abs(z) never gets larger than 2 (for n iterations).
    """
    z = 0
    for i in range(n):
        z = z**2 + c
        if(abs(z) > 2): 
            return False
    return True

assert inMSet(0 + 0j, 25) == True
assert inMSet(3 + 4j, 25) == False
assert inMSet(.3 + -.5j, 25) == True
assert inMSet(-.7 + .3j, 25) == False
assert inMSet(.42 + .2j, 25) == True
assert inMSet(.42 + .2j, 50) == False

def weWantThisPixel(col, row):
    """This function returns True if we want to show
       the pixel at col, row and False otherwise.
    """
    if col % 10 == 0  or  row % 10 == 0:
        return True
    else:
        return False

def test():
    """This function demonstrates how
       to create and save a PNG image.
    """
    width = 300
    height = 200
    image = PNGImage(width, height)

    # Create a loop that will draw some pixels.

    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col, row):
                image.plotPoint(col, row, (255,0,0))

    # We looped through every image pixel; we now write the file.
# changing and to or will make the dots into lines

    image.saveFile()

def scale(pix, pixMax, floatMin, floatMax):
    """scale accepts
           pix, the CURRENT pixel column (or row).
           pixMax, the total number of pixel columns.
           floatMin, the minimum floating-point value.
           floatMax, the maximum floating-point value.
       scale returns the floating-point value that
           corresponds to pix.
    """

    position = pix/pixMax
    return (floatMax-floatMin)*position + floatMin

def mset():
    """Creates a 300x200 image of the Mandelbrot set.
    """
    width = 300*1       # We can update the 1 later to enlarge the image...
    height = 200*1
    image = PNGImage(width, height)

    # Create a loop to draw some pixels

    for col in range(width):
        for row in range(height):
            # Use scale twice:
            #   once to create the real part of c (x)
            x = scale(col, 300, XMIN, XMAX)
            #   once to create the imaginary part of c (y)
            y = scale(row,200,YMIN, YMAX)
            # THEN, create c, choose n, and test:
            c = x + y*1j
            if inMSet(c, NUM_ITERATIONS) == True:
                image.plotPoint(col, row, (171, 50, 123))
            else:
                image.plotPoint(col,row, (0, 0, 0))


    # We looped through every image pixel; we now write the file
    image.saveFile()