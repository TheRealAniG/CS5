#
# hw6pr5.py -  Python!
#
#  Gold and Black:   this is "Intro to loops"! 
#
# Name: Anirudh Gupta
#
def fac(n):
    """Loop-based factorial function
       Argument: a nonnegative integer, n
       Return value: the factorial of n
    """
    result = 1                 # starting value - like a base case
    for x in range(1, n + 1):  # loop from 1 to n, inclusive
        result = result * x    # update the result by mult. by x
    return result              # notice this is AFTER the loop!

#
# Tests for looping factorial
#
print("fac(0) should be 1:", fac(0))
print("fac(5) should be 120:", fac(5))

def power(b,p):
    """Loop-based power function
       Arguments: numeric value(base b) and non-negative integer(power p)
       Return value: b**p
    """
    result = 1                 
    for x in range(1, p + 1):  
        result = result * b 
    return result              

#
# tests for looping power
#
print("power(2, 5): should be 32 ==", power(2, 5))
print("power(5, 2): should be 25 ==", power(5, 2))
print("power(42, 0): should be 1 ==", power(42, 0))
print("power(0, 42): should be 0 ==", power(0, 42))
print("power(0, 0): should be 1 ==", power(0, 0))

def summer(L):
    """Takes a list of number L and returns sum of all numbers in the list
    """
    result = 0                
    for x in L:
        result = result + x
    return result  

print("summer([10,10,10,2,10]): should be 42 ==", summer([10,10,10,2,10]))
print("summer([10,10,10,2]): should be 32 ==", summer([10,10,10,2]))
print("summer([11, 11]): should be 22 ==", summer([11,11]))
print("summer([47]): should be 47 ==", summer([47]))
print("summer([ ]): should be 0 ==", summer([ ]))

def summedOdds(L):
    """Takes a list of number L and returns sum of all odd elements in the list
    """
    result = 0              
    for x in L:
        if(x % 2 == 1):
            result = result + x
    return result

print( "summedOdds([4, 5, 6])      should be 5 :",  summedOdds([4, 5, 6]) )   
print( "summedOdds(range(3, 10))   should be 24 :",  summedOdds(range(3, 10)) )   


def summedExcept(exc, L):
    """Takes an integer exc and a list of integers L and returns the sum of list with everything except for exc
    """
    result = 0              
    for x in L:
        if(x != exc):
            result = result + x
    return result

# tests!
print( "summedExcept(5, [4, 5, 6])      should be 10 :",  summedExcept(5, [4, 5, 6]) )   
print( "summedExcept(5, [5, 5, 5])      should be 0 :",  summedExcept(5, [5, 5, 5]) ) 


def summedUpto(exc, L):
    """Takes an integer exc and a list of integers L and returns sum of all integers up to exc
    """
    result = 0              
    for x in L:
        if(x == exc):
            break
        else:
            result = result + x
    return result

# tests!
print( "summedUpto(5, [4, 5, 6])      should be 4 :",  summedUpto(5, [4, 5, 6]) )   
print( "summedUpto(5, [4, 6, 5])      should be 10 :",  summedUpto(5, [4, 6, 5]) ) 
print( "summedUpto(5, [4, 6, 32])     should be 42 :",  summedUpto(5, [4, 6, 32]) ) 




import random

def unique(L):
    """Decide whether all elements in L are unique.
       Argument: L, a list of any elements.
       Return value: True, if all elements in L are unique,
                  or False, if there is any repeated element
    """
    if len(L) == 0:
        return True
    elif L[0] in L[1:]:
        return False
    else:
        return unique(L[1:])  # recursion is OK in this function!

def untilARepeat(high):
    """Makes guesses from 0 to high and adds the guest to a list. 
       Keeps going until a guess is repeated and returns number of guesses
    """
    guess = random.choice(range(0, high))     
    L = [guess]                           
    while unique(L):
        guess = random.choice(range(0, high))
        L.append(guess)                  
    return len(L)

"""
In [85]: sum(L)/len(L)
Out[85]: 24.5021

In [86]: max(L)
Out[86]: 77

In [87]: min(L)
Out[87]: 2

In [88]: 42 in L
Out[88]: True

In [89]: L.count(2)
Out[89]: 26

In [90]: 1 in L
Out[90]: False

In [91]: 142 in L
Out[91]: False
"""

def rs():
    """One random step"""
    return random.choice([-1, 1])

def rwalk(radius):
    """Random walk between -radius and +radius  (starting at 0 by default)"""
    totalsteps = 0          # Starting value of totalsteps (_not_ final value!)
    start = 0               # Start location (_not_ the total # of steps)

    while True:             # Run "forever" (really, until a return or break)
        if start == -radius or start == radius:   
            return totalsteps # Phew!  Return totalsteps (stops the while loop)

        start = start + rs()
        totalsteps += 1     # addn totalsteps 1 (for all who miss Hmmm :-)

        #print("start:", start) # To see what's happening / debugging

    # it can never get here!


"""
Took less than a second to run rwalk(5) 10000 times
Took about a second to run rwalk(5) 100000 times
Took about 20 seconds to run rwalk(5) 1000000 times
The average in the list of 1,000,000 was 25.004946

In radius 5 takes on average about 25 steps to reach boundary
In radius 6 takes on average about 35.5 steps to reach boundary
In radius 7 takes on average about 49 steps to reach boundary
In radius 10 takes on average about 99 steps to reach boundary

In radius radius it takes about radius squared steps to reach the boundary on average
After num steps steps I would expect the walker to be the square root of num steps away from the starting point
"""

