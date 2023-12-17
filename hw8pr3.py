#
# hw8pr3.py
#

# Name: Anirudh Gupta

import random
import time
import math

#
# a function that throws one dart, returning true  (if it hits the circle)
#                                            false (otherwise)
#
def dart():
    """ Throws one dart between (-1,-1) and (1,1).
        Returns True if it lands in the unit circle; otherwise, False.
    """
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    if x**2 + y**2 < 1:
        return True        # HIT (within the unit circle)
    else:
        return False       # miss (landed in one of the corners)

def forpi(N):
    """Throws N darts, estimating pi."""
    pi = 42     # A suitably poor initial estimate
    throws = 0  # No throws yet 
    hits = 0    # No "hits" yet  (hits ~ in the circle)

    for x in range(N):
        if(dart() == True):
            throws += 1
            hits += 1
            pi = (4*hits/throws)
        else:
            throws +=1
            pi = (4*hits/throws)
        print(hits, "hits out of", throws,"throws so that pi is",pi)
    return pi


def whilepi(error):
    """Throws darts at the dartboard (the square) until the absolute difference 
       between the function's estimate of 𝝅 and the real value of 𝝅 is less than error.
    """
    piEstimate = 42
    throws = 0   
    hits = 0
    while(error < abs(math.pi - piEstimate)):
        if(dart() == True):
            throws += 1
            hits += 1
            piEstimate = (4*hits/throws)
        else:
            throws +=1
            piEstimate = (4*hits/throws)
        print(hits, "hits out of ", throws," throws so that pi is",piEstimate)
    return throws

def forpi_np(N):
    """Throws N darts, estimating pi."""
    pi = 42     # A suitably poor initial estimate
    throws = 0  # No throws yet 
    hits = 0    # No "hits" yet  (hits ~ in the circle)

    for x in range(N):
        if(dart() == True):
            throws += 1
            hits += 1
            pi = (4*hits/throws)
        else:
            throws +=1
            pi = (4*hits/throws)
    return pi


def whilepi_np(error):
    """Throws darts at the dartboard (the square) until the absolute difference 
       between the function's estimate of 𝝅 and the real value of 𝝅 is less than error.
    """
    piEstimate = 42
    throws = 0   
    hits = 0
    while(error < abs(math.pi - piEstimate)):
        if(dart() == True):
            throws += 1
            hits += 1
            piEstimate = (4*hits/throws)
        else:
            throws +=1
            piEstimate = (4*hits/throws)
    return throws

"""
ANSWERS TO QUESTIONS:
On average, how close to 𝝅 does forpi_np(N) get when N = 1
[4.0, 4.0, 0.0, 4.0, 4.0, 4.0, 4.0, 4.0]
3.116

On average, how close to 𝝅 does forpi_np(N) get when N = 10
[2.8, 2.0, 2.4, 2.8, 2.8, 3.6, 2.8, 2.0]
3.1283999999999903

On average, how close to 𝝅 does forpi_np(N) get when N = 100
[3.44, 3.12, 3.24, 3.0, 3.2, 3.16, 3.4, 2.96]
3.1406399999999883

On average, how close to 𝝅 does forpi_np(N) get when N = 1000
[3.16, 3.2, 3.124, 3.1, 3.16, 3.136, 3.236, 3.148]
3.1435679999999975

On average, how many throws are needed for whilepi_np(e) to get within e = 1
[1, 1, 1, 1, 3, 1, 1, 1]
1.805

On average, how many throws are needed for whilepi_np(e) to get within e = .1
[13, 5, 307, 49, 19, 13, 5, 5]
31.803

On average, how many throws are needed for whilepi_np(e) to get within e = .01
[33, 370, 14, 14, 14, 28, 120, 37]
667.313

On average, how many throws are needed for whilepi_np(e) to get within e = 0.001
[135, 447, 1932, 20745, 19833, 452, 652, 2453]
21970.455

Does forpi or whilepi estimate 𝝅 more efficiently? Why?
forpi is more efficient because the user decides how many throws so it can be as short as they want

Does forpi or whilepi estimate 𝝅 more accurately? Why?
whilepi is more accurate because it won't stop until the desired accuracy, so it can be as accurate as someone wants


"""