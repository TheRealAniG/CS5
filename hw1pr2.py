# CS5, Lab1 part 2
# Filename: hw1pr2.py
# Name: Anirudh Gupta
# Problem description: First few functions!


def dbl(x):
    """Result: dbl returns twice its argument
       Argument x: a number (int or float)
       Spam is great, and dbl("spam") is better!
    """
    return 2*x

def tpl(x):
    """Return value: tpl returns thrice its argument
       Argument x: a number (int or float)
    """
    return 3*x

def sq(x):
    """Return value: sq returns the square of its argument
       Argument x: a number (int or float)
    """
    return x*x

def interp(low, hi, fraction):
    """Return value: interp returns the fraction of the way between low and hi
       Argument low: floor valur, hi: ceiling valur fraction: how far between low and hi
    """
    return (hi-low)* fraction + low

def checkends(s):
    """Return value: returns true if first and last character are the same, false otherwise
       Argument s: a string
    """
    if(s[0]==s[-1]):
        return True
    else:
        return False
    
def has42(d):
    """Return value: returns true if key 42 is in dictionary, false otherwise
       Argument d: a dictionary
    """
    if 42 in d:
        return True
    else:
        return False
    
def hasKey(k,d):
    """Return value: returns True if key k is in dictionary d, false otherwise
       Argument k: key d: dictionary
    """
    if(k in d):
        return True
    else:
        return False
    
def flipside(s):
    """Return value: returns a string whose first half is s's second half and vice versa
       Argument s: a string
    """
    middle = len(s)//2

    return s[middle:] + s[:middle]

def convertFromSeconds(s):
    """Return value: a list of four integers that represents second in days, hours, minutes, and seconds
       Argument s: integer value representing seconds
    """
    days = s // (60 * 60 * 24)
    s = s - days * (60 * 60 * 24)
    hours = s // (60*60)
    s = s - hours * (60 * 60)
    minutes = s // 60
    seconds = s - minutes * (60)

    return [days, hours, minutes, seconds]
