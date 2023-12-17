# CS5, hw1pr3
# Filename: hw1pr3.py
#
# Name: Anirudh Gupta
# Problem description: Function Frenzy!
#

def mult(n,m):
    """mult returns n multiplied by m
       Arguments: n and m are integers
    """
    if m == 0:
        return 0
    elif m > 0:
        return n + mult(n, m-1)
    elif m < 0:
        return -n + mult(n, m + 1)
    
print( "mult(6, 7)           should be  42 :",  mult(6, 7) )
print( "mult(6, -7)          should be  -42 :",  mult(6, -7) )
print( "mult(-6, 7)          should be  -42 :",  mult(-6, 7) )
print( "mult(-6, -7)         should be  42 :",  mult(-6, -7) )
print( "mult(6, 0)           should be  0 :",  mult(6, 0) )
print( "mult(0, 7)           should be  0 :",  mult(0, 7) )
print( "mult(0, 0)           should be  0 :",  mult(0, 0) )


def dot(L, K):
    """dot returns the dot product of l and k
       Arguments L and K are both lists
    """
    if(len(L) != len(K)):
        return 0.0
    elif(len(L) == 0 and len(K) == 0):
        return 0.0
    elif(len(L) == 1 and len(K) == 1):
        return L[0] * K[0]
    else:
        return L[0] * K[0] + float(dot(L[1:], K[1:]))

#
# Tests
#
print()
print( "dot([5, 3], [6, 4])  should be  42.0 :",  dot([5, 3], [6, 4]) )
print( "dot([5, 3], [6])     should be  0.0 :",  dot([5, 3], [6]) )
print( "dot([], [6])         should be  0.0 :",  dot([], [6]) )
print( "dot([], [])          should be  0.0 :",  dot([], []) )
print( "dot([1, 2, 3, 4], [10, 100, 1000, 10000]) should be  43210.0 :",  dot([1, 2, 3, 4], [10, 100, 1000, 10000]) )

def ind(e, L):
    """ind returns the first index of e in L, if e is not in L it returns the length of L
       Arguments: e is an element, and L is a string or a list
    """
    if(len(L) == 0):
        return 0
    elif(L[0] == e):
        return 0
    else:
        return 1 + ind(e, L[1:])
    
#
# Tests
#
print()
print( "ind(42, [55, 77, 42, 12, 42, 100]) should be  2 :",  ind(42, [55, 77, 42, 12, 42, 100]) )
print( "ind(55, [55, 77, 42, 12, 42, 100]) should be  0 :",  ind(55, [55, 77, 42, 12, 42, 100]) )
print( "ind(42, list(range(0, 100)))       should be  42 :",  ind(42, list(range(0, 100))) )
print( "ind('hi', ['hello', 42, True])     should be  3 :",  ind('hi', ['hello', 42, True]) )
print( "ind('hi', ['well', 'hi', 'there']) should be  1 :",  ind('hi', ['well', 'hi', 'there']) )
print( "ind('i', 'team')                   should be  4 :",  ind('i', 'team') )
print( "ind(' ', 'outer exploration')      should be  5 :",  ind(' ', 'outer exploration') )

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
    
#
# Tests
#
print()
print( "letterScore('h') should be  4 :",  letterScore('h') )
print( "letterScore('c') should be  3 :",  letterScore('c') )
print( "letterScore('a') should be  1 :",  letterScore('a') )
print( "letterScore('z') should be 10 :",  letterScore('z') )
print( "letterScore('^') should be  0 :",  letterScore('^') )
print( "letterScore('X') should be  8 :",  letterScore('X') )

def scrabbleScore(S):
    """scrabbleScore takes a String and returns the scrabble score of that string
       Argument: S is a string
    """
    if(len(S) == 0 ):
        return 0
    else:
        return letterScore(S[0]) + scrabbleScore(S[1:])
    
print()
#
# Tests
#
print( "scrabbleScore('quetzal')           should be  25 :",  scrabbleScore('quetzal') )
print( "scrabbleScore('jonquil')           should be  23 :",  scrabbleScore('jonquil') )
print( "scrabbleScore('syzygy')            should be  25 :",  scrabbleScore('syzygy') )
print( "scrabbleScore('?!@#$%^&*()')       should be  0 :",  scrabbleScore('?!@#$%^&*()') )
print( "scrabbleScore('')                  should be  0 :",  scrabbleScore('') )
print( "scrabbleScore('abcdefghijklmnopqrstuvwxyz') should be  87 :",  scrabbleScore('abcdefghijklmnopqrstuvwxyz') )

def one_dna_to_rna(c):
        """Converts a single-character c from DNA
           nucleotide to its complementary RNA nucleotide
        """
        # dictionary with each conversion
        conversion = { 'A':'U', 'C':'G', 'G':'C', 'T':'A' }
        #
        # check if the input, c, is a key in the dictionary
        if c in conversion:        # is it a key?
            return conversion[c]   # if so, return its value
        else:                      # otherwise
            return ''              # return the empty string
        
def transcribe(S):
    """Takes a string of DNA and returns the string of the messenger RNA, removing any unwanted characters
       Argument: S is a string
    """
    if(len(S) == 0 ):
        return ""
    else:
        return one_dna_to_rna(S[0]) + transcribe(S[1:])
    
print()
#
# Tests
#
print( "transcribe('ACGTTGCA')             should be  'UGCAACGU' :",  transcribe('ACGTTGCA') )
print( "transcribe('ACG TGCA')             should be  'UGCACGU' :",  transcribe('ACG TGCA') )  # Note that the space disappears
print( "transcribe('GATTACA')              should be  'CUAAUGU' :",  transcribe('GATTACA') )
print( "transcribe('cs5')                  should be  ''  :",  transcribe('cs5') ) # Note that other characters disappear
print( "transcribe('')                     should be  '' :",  transcribe('') )   # Empty strings!

# assert statements!  See below for details...
assert transcribe('ACGTTGCA') == 'UGCAACGU'
assert transcribe('ACG TGCA') == 'UGCACGU'   # Note that the space disappears
assert transcribe('GATTACA')  == 'CUAAUGU'
assert transcribe('cs5')      == ''        # Note that non-DNA other characters disappear
assert transcribe('')         == ''

