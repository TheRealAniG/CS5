# CS5, hw4pr1
# Filename: hw4pr1.py
# Name: Anirudh Gupta
# Problem description: Binary <-> decimal conversions

def isOdd(N):
    """Acccepts a single interger, N, and returns true is N is odd and False if
       N is even
    """
    return N % 2 == 1

print("isOdd(42)    should be  False :", isOdd(42))
print("isOdd(43)    should be  True :", isOdd(43))


def numToBinary(N):
    """Takes an integer and returns a string of the binary conversion
    """
    if N == 0:
        return ''
    elif N%2 == 1:
        return numToBinary((N-1)/2) + '1'
    else:
        return numToBinary(N/2) + '0'


print("numToBinary(0)      should be  '' :",  numToBinary(0))
print("numToBinary(42)     should be  '101010' :",  numToBinary(42))

def binaryToNum(S):
    """Takes a string of binary digits and converts it into the base 10 number
    """
    if S == '':
        return 0

    # if the last digit is a '1'...
    elif S[0] ==  '1':
        return binaryToNum(S[1:]) + (2**(len(S)-1))

    else: # last digit must be '0'
        return binaryToNum(S[1:]) + 0
    

# tests

print("binaryToNum('')     should be  0 :",  binaryToNum(''))
print("binaryToNum('101010') should be  42 :",  binaryToNum('101010'))

def increment(S):
    """Accepts a 8 character string of binary digits and returns the
       next largest number in binary
    """
    if(S == "11111111"): return "00000000"
    else:
        incrementedBinary = numToBinary(binaryToNum(S) + 1)
        while(len(incrementedBinary) < 8):
            incrementedBinary = "0" + incrementedBinary
        return incrementedBinary

    
print("increment('00101001')    should be  00101010 :", increment('00101001'))
print("increment('00000011')    should be  00000100 :", increment('00000011'))
print("increment('11111111')    should be  00000000 :", increment('11111111'))

def count(S,n):
    """Acccepts 8-character binary string,S, and counts n time upward from S,
       printing as it goes
    """
    if n == -1: return 
    else:
        print(S)
        count(increment(S), n - 1)

"""
The Ternary representation for 59 is 2012,
This is because 2*27 + 9*0 + 3*1 + 1*2 = 59
"""

def numToTernary(N):
    """Returns a ternary sting representing the value of argument N
    """
    if N == 0:
        return ''
    elif N%3 == 2:
        return numToTernary((N-2)/3) + '2'
    elif N%3 == 1:
        return numToTernary((N-1)/3) + '1'
    else:
        return numToTernary(N/3) + '0'
    
def ternaryToNum(S):
    """Returns the value equivalent to the string S, when S is interpreted in
       ternary
    """
    if S == '':
        return 0

    elif S[0] ==  '2':
        return ternaryToNum(S[1:]) + 2*(3**(len(S)-1))
    elif S[0] ==  '1':
        return ternaryToNum(S[1:]) + (3**(len(S)-1))
    else:
        return ternaryToNum(S[1:]) + 0

def balancedTernaryToNum(S):
    """Returns the decimal value equivalent to the balanced ternary string s
    """
    if S == '':
        return 0
    elif S[0] ==  '+':
        return balancedTernaryToNum(S[1:]) + (3**(len(S)-1))
    elif S[0] ==  '-':
        return balancedTernaryToNum(S[1:]) - (3**(len(S)-1))
    else:
        return balancedTernaryToNum(S[1:]) + 0
    
def numToBalancedTernary(N):
    """Returns the balanced ternary string represing the value of argument N
    """
    if N == 0:
        return ''
    elif N%3 == 2:
        return numToBalancedTernary((N-2)/3 + 1) + '-'
    elif N%3 == 1:
        return numToBalancedTernary((N-1)/3) + '+'
    else:
        return numToBalancedTernary(N/3) + '0'

