#
# hw3pr2.py - algorithms and use-it-or-lose-it
#

print("Onward, Algorithms!")

# The NEXT_CHAR dictionary for use in rotc(c)
#
NEXT_CHAR = { "a": "b", "A": "B",
              "b": "c", "B": "C",
              "c": "d", "C": "D",
              "d": "e", "D": "E",
              "e": "f", "E": "F",
              "f": "g", "F": "G",
              "g": "h", "G": "H",
              "h": "i", "H": "I",
              "i": "j", "I": "J",
              "j": "k", "J": "K",
              "k": "l", "K": "L",
              "l": "m", "L": "M",
              "m": "n", "M": "N",
              "n": "o", "N": "O",
              "o": "p", "O": "P",
              "p": "q", "P": "Q",
              "q": "r", "Q": "R",
              "r": "s", "R": "S",
              "s": "t", "S": "T",
              "t": "u", "T": "U",
              "u": "v", "U": "V",
              "v": "w", "V": "W",
              "w": "x", "W": "X",
              "x": "y", "X": "Y",
              "y": "z", "Y": "Z",
              "z": "a", "Z": "A",
}

def letterScore(let):
    """letter score takes a single character argument and returns its score in scrabble. If its not a letter it returns 0
       Argument: let is a string
    """
    if let in 'aeioulnrstAEIOULNRST':
        return 1
    elif let in 'dgDG':
        return 2
    elif let in 'bcmpBCMP':
        return 3
    elif let in 'fhvwyFHVWY':
        return 4
    elif let in 'kK':
        return 5
    elif let in 'jxJX':
        return 8
    elif let in 'zqZQ':
        return 10
    else: 
        return 0
    
def scrabbleScore(S):
    """scrabbleScore takes a String and returns the scrabble score of that string
       Argument: S is a string
    """
    if(len(S) == 0 ):
        return 0
    else:
        return letterScore(S[0]) + scrabbleScore(S[1:])


# The function shift1(c)

def shift1(c):
    """ rotate 1 character, c, by 1 place 
        c must be 1 character.
        non-characters don't change!
    """
    if c not in NEXT_CHAR:   # if c is NOT there,
        return c             # just return it unchanged
    else:
        return NEXT_CHAR[c]  # else return the next char
    

def encipher(s, N):
    """s is a string and whose second argument N is a non-negative integer between 0 and 25
       Encipher returns a new string in which the letters in s have been "rotated" by N characters 
       forward in the alphabet, wrapping around when needed
    """

    if N == 0:
        return str.join("",s)
    else:
        s = [shift1(x) for x in s]
        return encipher(s, N - 1)
    
print("encipher('xyza', 1) == 'yzab'", encipher('xyza', 1))
print("encipher('Z A', 1) == 'A B'", encipher('Z A', 1))

assert encipher('xyza', 1) == 'yzab'
assert encipher('Z A', 1) == 'A B'

#I used the string with the lowest scrabble score out of all 26 options since that seems to yield the actual message most times
def decipher(s):
    """Decipher takes in a enciphered string s.
       It returns the deciphered string"""
    LC = [encipher(s,n) for n in range(26)]
    SC = [scrabbleScore(x) for x in LC]
    index = SC.index(min(SC))
    word = LC[index]
    return word


def count(e, L):
    """E is a value and L is a list
       returns how many times e appears in L
    """
    LC = [1 for x in L if x == e]
    return sum(LC)

def blsort(L):
    """L is a binary list
       We return L sorted in ascending order
    """

    ones = count(1, L)
    zeroes = count(0, L)
    stringlist= list("0"*zeroes + "1"*ones)
    return [int(x) for x in stringlist]


def gensort(L):
    """Takes in a list L and returns a new list in ascending order
    """
    if(len(L) == 0):
        return L
    elif len(L) == 1: 
        return L
    else:
        minimum = min(L)
        mindex = L.index(min(L))
        print(minimum)
        return [minimum] + gensort(L[:mindex]+L[mindex + 1:])
    
def jscore(S, T):
    """Accepts two strings S and T
       Returns the number of characters shared by S and T
    """

    if (len(S) == 0 or len(T) == 0):
       return 0
    else:
        if(S[0] in T):
            return 1 + jscore(S[1:], (T[:T.index(S[0])] + T[T.index(S[0]) + 1:]))
        else:
            return 0 + jscore(S[1:], T)


def exact_change(target_amount, L):
    """Target_amount is a non-negative integer, and L is a list of positive integers
       exact_change returns True if its possible to make the target_amount with the
       values in L
    """
    if(target_amount == 0 ): return True
    elif(target_amount < 0): return False
    elif(sum(L) < target_amount): return False
    else:
        loseit = exact_change(target_amount, L[1:])
        useit = exact_change(target_amount - L[0], L[1:])
        if(useit == True or loseit == True): return True
        else: return False

def LCS(S, T): 
    """Accepts two strings S and T
       returns the longest common subsequence that S and T share
    """
    if(len(S) == 0 or len(T) == 0): return ""
    elif(S[0] == T[0]): 
        return S[0] + LCS(S[1:],T[1:])
    else:
        loseit1 = LCS(S[1:], T)
        loseit2 = LCS(S, T[1:])
        if(len(loseit1) > len(loseit2)):
            return loseit1
        else:
            return loseit2



