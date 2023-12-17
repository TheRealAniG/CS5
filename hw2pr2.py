# CS5 Black, hw2pr2
# Filename: hw2pr2.py
# Name: Anirudh Gupta
# Problem description: Sleepwalking student

import random  

def rs():
    """rs chooses a random step and returns it.
       Note that a call to rs() requires parentheses.
       Arguments: none at all!
    """
    return random.choice([-1, 1])

import time

def rwpos(start, nsteps):
    """ rwpos models a random walker that
        * starts at the int argument, start
        * takes the int # of steps, nsteps

        rwpos returns the final position of the walker.
    """
    time.sleep(0.1)
    print('location is', start)
    if nsteps == 0:
        return start
    else:
        newpos = start + rs()  # take one step
        return rwpos(newpos, nsteps - 1)


import time
import sys

def rwsteps(start, low, hi):
    """ rwsteps models a random walker which
        * is currently at start 
        * is in a walkway from low (usually 0) to hi (max location) 
          
        rwsteps returns the # of steps taken 
        when the walker reaches an edge

        Backstory: A computer science student at HMC finds himself sleepwalking after dinner at the Hoch.
        He needs to find his way to either the Mcgregor computer science lab or his dorm in order to finish his CS5 homework.
        He is walking randomly so the faster he gets to either location the earlier he can get his homework done and sleep.
    """
    walkway = "_"*(hi-low)    # create a walkway of underscores
    S = (start-low)           # this is our sleepwalker's location, start-low

    walkway = "🖥️" + walkway[:S] + "🧍" + walkway[S:] + "🏠"  # put our sleepwalker, "S", there

    walkway = " " + walkway + " "              # surround with spaces, for now...

    print(walkway, "    ", start, low, hi)     # print everything to keep track...
    time.sleep(0.1)

    if start <= low or start >= hi:            # base case: no steps if we're at an endpt
        return 0
    
    else:
        newstart = start + rs()                # takes one step, from start to newstart
        return 1 + rwsteps(newstart, low, hi)  # counts one step, recurses for the rest!
    
def rw2steps(start1, start2, low, hi):
    """ This simulator observes two walkers, racing to reach 
        their dorm room first. 
        
        Returns the step when either student reaches their dorm first

        start1:  the location of the first student
        start2:  the location of the second student 
        start1 must be less than start2 
        low: the location of the first students dorm
        hi: the location of the second students dorm

        The dorms do not not move.
        If the students are at the same place they bounce off each other with student 1 going left and student 2 going right
   
        Good values to run: rw2steps( 5, 15, 0, 20 )  # student 1 is to the left of student 2
                            Any values where student 1 starts to the left of student 2 is a good value to run. If not it won't work

                
        In [85]: rw2steps(5,15,0, 20)
        🏠_____🧍__________🧍_____🏠       5 15 0 20
        🏠______🧍________🧍______🏠       6 14 0 20
        🏠_____🧍________🧍_______🏠       5 13 0 20
        🏠______🧍________🧍______🏠       6 14 0 20
        🏠_______🧍________🧍_____🏠       7 15 0 20
        🏠______🧍__________🧍____🏠       6 16 0 20
        🏠_______🧍________🧍_____🏠       7 15 0 20
        🏠________🧍________🧍____🏠       8 16 0 20
        🏠_________🧍________🧍___🏠       9 17 0 20
        🏠__________🧍________🧍__🏠       10 18 0 20
        🏠_________🧍__________🧍_🏠       9 19 0 20
        🏠________🧍__________🧍__🏠       8 18 0 20
        🏠_________🧍________🧍___🏠       9 17 0 20
        🏠__________🧍________🧍__🏠       10 18 0 20
        🏠___________🧍______🧍___🏠       11 17 0 20
        🏠____________🧍______🧍__🏠       12 18 0 20
        🏠___________🧍________🧍_🏠       11 19 0 20
        🏠____________🧍______🧍__🏠       12 18 0 20
        🏠_____________🧍____🧍___🏠       13 17 0 20
        🏠____________🧍____🧍____🏠       12 16 0 20
        🏠___________🧍____🧍_____🏠       11 15 0 20
        🏠__________🧍______🧍____🏠       10 16 0 20
        🏠___________🧍____🧍_____🏠       11 15 0 20
        🏠____________🧍__🧍______🏠       12 14 0 20
        🏠___________🧍____🧍_____🏠       11 15 0 20
        🏠__________🧍____🧍______🏠       10 14 0 20
        🏠_________🧍____🧍_______🏠       9 13 0 20
        🏠__________🧍__🧍________🏠       10 12 0 20
        🏠___________🧍🧍_________🏠       11 11 0 20
        🏠__________🧍__🧍________🏠       10 12 0 20
        🏠___________🧍__🧍_______🏠       11 13 0 20
        🏠__________🧍____🧍______🏠       10 14 0 20
        🏠_________🧍______🧍_____🏠       9 15 0 20
        🏠________🧍________🧍____🏠       8 16 0 20
        🏠_________🧍________🧍___🏠       9 17 0 20
        🏠________🧍__________🧍__🏠       8 18 0 20
        🏠_______🧍____________🧍_🏠       7 19 0 20
        🏠________🧍____________🧍🏠       8 20 0 20
        Out[85]: 37

        In [86]: rw2steps(3,10,0, 20)
        🏠___🧍_______🧍__________🏠       3 10 0 20
        🏠__🧍_________🧍_________🏠       2 11 0 20
        🏠___🧍_______🧍__________🏠       3 10 0 20
        🏠__🧍_________🧍_________🏠       2 11 0 20
        🏠___🧍_______🧍__________🏠       3 10 0 20
        🏠__🧍_________🧍_________🏠       2 11 0 20
        🏠_🧍___________🧍________🏠       1 12 0 20
        🏠__🧍_________🧍_________🏠       2 11 0 20
        🏠_🧍___________🧍________🏠       1 12 0 20
        🏠🧍_____________🧍_______🏠       0 13 0 20
        Out[86]: 9
    """
    walkway = "_"*(hi-low)    # create a walkway of underscores
    S1 = (start1-low)           # this is our sleepwalker's location, start-low
    S2 = (start2 - low)

    walkway = "🏠" + walkway[:S1] + "🧍" + walkway[S1:S2] + "🧍" + walkway[S2:] + "🏠"  # put our sleepwalker, "S", there

    walkway = " " + walkway + " "              # surround with spaces, for now...

    print(walkway, "    ", start1, start2, low, hi)     # print everything to keep track...
    time.sleep(0.05)

    if start1 <= low or start1 >= hi or start2 <= low or start2 >= hi:            # base case: no steps if we're at an endpt
        return 0
    elif(start2 == start1):
        newstart1 = start1 - 1                # takes one step, from start to newstart
        newstart2 = start2 + 1
        return 1 + rw2steps(newstart1, newstart2, low, hi)  # counts one step, recurses for the rest!
    
    else:
        newstart1 = start1 + rs()                # takes one step, from start to newstart
        newstart2 = start2 + rs()
        return 1 + rw2steps(newstart1, newstart2, low, hi)  # counts one step, recurses for the rest!
