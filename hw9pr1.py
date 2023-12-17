#
# hw9pr1.py - Game of Life lab (Conway)
#
# Name:
#

import random

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You might use this in your createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """Returns a 2D array with "height" rows and "width" columns."""
    A = []
    for row in range(height):
        A += [createOneRow(width)]  # Use the above function so that SOMETHING is one row!
    return A

def printBoard(A):
    """This function prints the 2D list-of-lists A."""
    for row in A:                # row is the whole row
        for col in row:          # col is the individual element
            print(col, end = '') # Print that element
        print()

def diagonalize(width, height):
    """Creates an empty board and then modifies it
       so that it has a diagonal strip of "on" cells.
       But it does that only in the *interior* of the 2D array.
    """
    A = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A

def innerCells(w, h):
    """Creates an empty board and then modifies it
       so that it has all live cells.
       But it does that only in the *interior* of the 2D array.
    """
    A = createBoard(w, h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
                A[row][col] = 1
    return A

def randomCells(w, h):
    """Creates an empty board and then modifies it
       so that it has random live cells.
       But it does that only in the *interior* of the 2D array.
    """
    A = createBoard(w, h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
                A[row][col] = random.choice([0, 1])
    return A

def copy(A):
    """Returns a DEEP copy of the 2D array A."""
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            newA[row][col] = A[row][col] # What should be here, in order to
            # ..copy each element of A into the corresponding spot in newA?

    return newA


def innerReverse(A):
    """Returns a reversed version of the 2D array A except for the border."""
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if(A[row][col] == 1):
                newA[row][col] = 0 
            else:
                newA[row][col] = 1
    return newA

def countNeighbors(row,col,A):
    """Counts the number of live cells around the desired location
    """
    count = 0
    for i in range(row-1, row + 2):
        for j in range(col-1, col + 2):
            if(i >= 0 and j >= 0 and i <= len(A) and j <= len(A[0])):
                if(A[i][j] == 1):
                    count += 1
    if(A[row][col] == 1): count -= 1 
    return count

def next_life_generation(A):
    """Makes a copy of A and then advances one
       generation of Conway's Game of Life within
       the *inner cells* of that copy.
       The outer edge always stays at 0.
    """

    newA = copy(A)
    for row in range(1, len(A)-1):
        for col in range(1, len(A[0])-1):
            neighbors = countNeighbors(row,col,A)
            if(neighbors < 2):
                newA[row][col] = 0
            elif(neighbors > 3):
                newA[row][col] = 0
            elif(neighbors == 3):
                newA[row][col] = 1
            else:
                newA[row][col] = A[row][col]
    return newA











#
# +++ Helper functions for when Life has been completed! +++
#

"""
These allow for "terminal-graphics animation"

Once next_life_generation is complete, run

   lifedemo()

You may need to adjust your terminal's shape/size to 
    create a smooth animation.

"""

import sys

def printBoard_with_d( A, d = None ):
    """ this function prints the 2d list-of-lists A
        using the dictionary d 
    """
    if (d == None) or (0 not in d) or (1 not in d): # can we use d?
        for row in A:
            for col in row:
                sys.stdout.write( str(col) )     # use raw contents
            sys.stdout.write( '\n' )
    else:
        for row in A:
            for col in row:
                sys.stdout.write( str(d[col]) )  # lookup each value
            sys.stdout.write( '\n' )

def placeGlider(row,col,A):
    """ creates a glider with a bounding box
        whose upper-left corner is at row row and col col
    """
    H = len(A); W = len(A[0])
    OFFSETS = [ [+0,+1], [+1,+2], [+2,+0], [+2,+1], [+2,+2] ]
    for row_offset, col_offset in OFFSETS:
        r = row + row_offset
        c = col + col_offset
        if 0 < r < H-1 and 0 < c < W-1:
            A[r][c] = 1
    # no need to return A, A is changed in place!

def placeAirDancer(row,col,A):
    """ creates an up-down air dancer with top location
        (upper-left corner) is at row row and col col
    """
    H = len(A); W = len(A[0])
    OFFSETS = [ [+0,+0], [+1,+0], [+2,+0] ]
    for row_offset, col_offset in OFFSETS:
        r = row + row_offset
        c = col + col_offset
        if 0 < r < H-1 and 0 < c < W-1:
            A[r][c] = 1
    # no need to return A, A is changed in place!

import time

def lifedemo():
    """ ASCII demo! 
    """
    W = 42; H = 21          # alter to suit!
    
    A = createBoard(W,H)    # empty grid
    placeGlider(2,2,A)
    placeAirDancer(2,20,A)
    placeAirDancer(3,36,A)

    # A = randomCells(W,H)   # random grid
    
    # dictionaries to indicate what to print
    # d = { 0: 0,    1: 1 }
    d = { 0: 0,    1: " " }
    # d = { 0: " ",  1: "0" }
    # d = { 0: " ",  1: "#" }
    # d = { 0: "▯", 1: "▮" }
    # d = { 0: " ",  1: "🙂" } 


    while True:
        print("\n")

        
        printBoard_with_d(A, d)
        print("\n")
        A = next_life_generation(A)
        time.sleep(0.42)


# the terminal colors don't seem as successful
# d = { 0: "\033[6;36;47m0\033[0m", 1: "\033[6;37;40m1\033[0m" }
# www.cs.hmc.edu/twiki/bin/view/CS5/TerminalColorsInPython


#
# +++ end of helper functions +++
#