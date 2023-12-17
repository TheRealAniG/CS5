# Anirudh Gupta

def numToBaseB(N, B):
    """Arguments are a non-negative integer N and a base B (between 2 and 10 inclusive)
       Returns a string representing the number N in base B.
    """
    remainder = N % B
    if(N == 0):
        return ""
    else:
        return numToBaseB(N//B, B) + str(remainder)
    
def baseBToNum(S, B):
    """Arguments are a string S and a base B, where S represents a number in base B, and where B is between 2 and 10 inclusive.
       baseBToNum should then return an integer in base 10 representing the same number as S.
    """
    if S == '':
        return 0
    else:
        return baseBToNum(S[1:], B) + int(S[0])*B**(len(S)-1)
    
def baseToBase(B1, B2, s_in_B1):
    """Three arguments: a base B1, a base B2 (both of which are between 2 and 10, inclusive) and s_in_B1, 
       which is a string representing a number in base B1. Returns a string representing the same number in base B2.
    """

    return numToBaseB(baseBToNum(s_in_B1, B1),B2)

assert baseToBase(2, 4, '101010') == '222'
assert baseToBase(2, 5, '1001001010') == '4321'

def add(S,T):
    """Takes two binary strings S and T and returns their sum, also in binary.
    """
    num1 = baseBToNum(S, 2)
    num2 = baseBToNum(T, 2)
    num3 = num1 + num2
    return numToBaseB(num3, 2)

def addB(S, T):
    """S and T are binary strings, and addB adds them returning a binary number
    """

    if(S == ""): return T
    if(T == ""): return S
    else:
        if S[-1] == '0' and T[-1] == '0':
            return addB(S[:-1], T[:-1]) + '0'
        elif S[-1] == '1' and T[-1] == '0':
            return addB(S[:-1], T[:-1]) + '1'
        elif S[-1] == '0' and T[-1] == '1':
            return addB(S[:-1], T[:-1]) + '1'
        else: 
            first = addB("1", S[:-1])
            return addB(first, T[:-1])  + '0'

assert addB('11', '100') == '111'
assert addB("11100", "11110") == '111010'
assert addB('110','11') == '1001'
assert addB('110101010','11111111') == '1010101001'
assert addB('1','1') == '10'

def countFirstRepeats(S):
    """Counts how many times the first character repeats in a row in string S
    """
    if(S == ""): return 0
    elif(len(S) == 1): return 1
    else:
        if(S[0]== S[1]): return countFirstRepeats(S[1:]) + 1
        else:
            return 1
    

def compress(S):
    """Argument is a binary string S of length less than or equal to 64
       Returns a run-length encoding of the original in binary
    """
    if(len(S)>0):
        b_or_w = S[0]
    if(len(S)== 0): return ""
    else:
            return b_or_w + numToBaseB(countFirstRepeats(S), 2).zfill(7) + compress(S[countFirstRepeats(S):])

def uncompress(C):
    """Takes a string C and undoes the compress function
    """
    if(len(C)>0):
        b_or_w = C[0]
    if(len(C)== 0): return ""
    else:
        return b_or_w * baseBToNum(C[1:8], 2) + uncompress(C[8:])