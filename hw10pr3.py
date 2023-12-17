# coding: utf-8
#
# The top line, above, is important -- it ensures that Python will be
# able to use this file even if you paste in text with fancy Unicode
# characters that aren't part of normal ASCII.
#
# For another example of such a file, see
# https://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt
#
# OK! Now we're ready for hw10pr3.py ...
#
# Name: Anirudh Gupta
#

#
# First, some helper/example functions for files + text ...
#
# To make the examples work, you should have the text file named "a.txt"
# in the same directory as this .py file!
#
# If you _don't_ have "a.txt", create it.  Here are its contents:
"""
I like poptarts and 42 and spam.
Will I get spam and poptarts for
the holidays? I like spam poptarts!
"""
import random


def get_text(filename):
    """Opens a file named 'filename', reads
       it, and returns its contents (as one big string).

       Example:
          In [1]: get_text("a.txt")
          Out[1]: 'I like poptarts and 42 and spam.\nWill I get spam and poptarts for\nthe holidays? I like spam poptarts!\n\n\n\n'

          In [1]: len(get_text("a.txt"))
          Out[1]: 102  # Well, _around_ 102, depending how many \n's you have at the end of a.txt.
                       # Note that '\n' is ONE character:   len('\n') == 1
    """
    #
    # First we have to open the file (just like opening a book to read it).
    # We assume the "utf-8" encoding, which accepts more characters than plain ASCII
    #
    # Other common codings welcome, e.g., utf-16 or latin1
    # See [docs.python.org/3.8/library/codecs.html#standard-encodings]
    # for the full list (it's big!).
    #
    f = open(filename, encoding = 'utf-8')

    #
    # Read the contents of the file into a string named "text", close
    # the file, and return the string.
    #
    text = f.read()
    f.close()
    return text

def word_count(text):
    """Word-counting function.
       Counts the number of "words" (space-separated sequences) in
       the string "text".

       Examples:
          In [1]: word_count('This has four words!')
          Out[1]: 4

          In [1]: word_count(get_text("a.txt"))
          Out[1]: 20                 # If it's the a.txt file above
    """
    #
    # The text of the file is one long string.  Use "split" to get words!
    #
    LoW = text.split()    # We could use text.split("\n") to get _lines_.

    #
    # LoW is a List of Words, so its length is the word count.
    #
    result = len(LoW)

    # Comment out, as needed...
    if result < 100:
        print("LoW[0:result] is", LoW[0:result])  # For sanity checking...
    else:
        print("LoW[0:100] is", LoW[0:100])        # without going too far...

    return result



# Use the string library to implement remove_punctuation:
import string    # See https://docs.python.org/3/library/string.html
                 # Note: str is different: docs.python.org/3/library/stdtypes.html#textseq

def remove_punctuation(text):
    """Accepts a string named "text".  Returns an equivalent string, _but_
       with all non-(English)-text characters removed (keeps only
       letters + digits).

       + Vary to suit the language at hand!

       Examples:
          In [1]: remove_punctuation("42_isn't_.!?41.9bar")
          Out[1]: '42isnt419bar'

          In [2]: remove_punctuation(get_text("a.txt"))
          Out[2]: 'Ilikepoptartsand42andspamWillIgetspamandpoptartsfortheholidaysIlikespampoptarts' # (Not so useful w/o spaces!)
    """
    new_text = ''
    CHARS_TO_KEEP = string.ascii_letters + string.digits # + string.whitespace + string.punctuation
    for c in text:  # c is each character
        # Use the Python string library
        if c in CHARS_TO_KEEP:
            new_text += c
        else:
            pass # don't include it  [WARNING: as written, this removes spaces!]

    # We're finished!
    return new_text


def vocab_count(text):
    """Returns a dictionary of (punctuationless, lower-cased) words in "text".

       + Removes everything not in string.ascii_letters (via the function
         above).
       + Also, lower-cases everything (alter to suit your taste or
         application!).
       + Builds and returns a dictionary of how many times each word occurs.

       Examples:
          In [1]: vocab_count("Spam, spam, I love spam!")
          There are 5 words.
          There are 3 *distinct* words in the text.

          Out[1]: {'spam': 3, 'i': 1, 'love': 1}


          In [2]: vocab_count(get_text("a.txt"))
          There are 20 words.
          There are 11 *distinct* words in the text.

          Out[2]:
                    {'i': 3,
                    'like': 2,
                    'poptarts': 3,
                    'and': 3,
                    '42': 1,
                    'spam': 3,
                    'will': 1,
                    'get': 1,
                    'for': 1,
                    'the': 1,
                    'holidays': 1}
    """
    LoW = text.split()
    print("There are", len(LoW), "words.")  # For info - comment out if you like

    d = {}
    for word in LoW:
        word = remove_punctuation(word)  # Remove punctuation!
        word = word.lower()   # Make lower case!

        if word not in d:     # If it's not already in the dictionary, d
            d[word] = 1       # Set count to 1  (the VALUE is the count, here)
        else:                 # ..or if it IS already in the dictionary, d
            d[word] += 1      # ..add 1 to count (again, the VALUE is the count)

    print("There are", len(d), "*distinct* words in the text.\n")
    return d            # This way we can _use_ or look up the keys in d...




"""
[a] What was in the file you analyzed?   -->    The Declaration of Independence
    + Feel free to include it (up to you).

[b] How many words did it have?  -->     1336
    Use word_count.

[c] How many characters did it have?  -->       8113

    Note: there's no function for this, but len(get_text("a.txt")) will do it!


[d] How many _distinct_ words did it have?  -->       536
    Use vocab_count.
    Adapt as you see fit...

[e] What are three words that appeared unusually often for this text?  --> states, people, laws
    - ...relative to a generic distribution of "all text"

    For example, it's _not_ unusual if "the" or "a" are the
    most common words in an English text.


[f] Other thoughts/insights?!
There are words that appear much more often, but they are words like "the", and "and".
Its not common for states, people, and laws to appear very often

"""

#
# Now, to the Markov modeling (createDictionary) and Markov text
# generation (generateText)
#
# Be sure to create your 500-word "CS-Essay,"" with:
#    In [1]: d = createDictionary(get_text("yourfile.txt"))
#    In [2]: generateText(d, 500)       # Then copy the "essay" below ...
#

#
# Function #1  (createDictionary)
#
def createDictionary(text):
    """accepts a string of text and returns the Markov Model dictionary out of the string
    """
    LoW = text.split()

    d = {}
    pw = '$'   # pw indicates previous word

    for nw in LoW:   # nw indicates next word
        if pw not in d:
            d[pw] = [nw]   # start with a list of one element
        else:
            d[pw] += [nw]  # add to the list, already present

        pw = nw     # before re-looping, assign pw to be the just-handled "new" word (nw)

        if pw[-1] in '.!?':
            pw  = '$'
        #
        # Here, check for whether that new previous word, pw, ends in 
        # punctuation -- if it _does_ then set pw to be '$'
        # that way, it will be back at the start of a new sentence!
        #

    return d


#
# Function #2   (generateText)
#
def generateText(d, N):
    """accepts a dictionary of word transitions,d, and a positive integer n
       Prints a string of n words, where text is autogenerated using first
       order markov text generator.
    """
    print()  # start by printing a newline

    previousWord = "$"
    for i in range(N):
        next_word = random.choice(d[previousWord])  # Next word -- will be replaced (alas)
        # Here's how to print so that things don't always start on the next line
        # Using end = ' ' stops it going to the next line
        print(next_word, end = ' ')
        previousWord = next_word
        if(previousWord[-1] in '.!?'):
            previousWord = "$"

    print()                  # Final print, newline


#
# Your 500-or-so-word "CS Essay" (paste into the triple-quoted strings below):
#
"""
The Declaration of Independence by Thomas Jefferson

Highlight: Nothing specific, but I am surprised how readable it is. Not too bad for a simple text generator


A Prince, whose known rule of peace, Standing Armies without our Separation, and waging War against us.
He has combined with a Tyrant, is their operation till his Protection and superior to Laws, 
the conditions of Government here, by Authority of Happiness. He has excited domestic insurrections 
amongst us, in the protection of these truths to a multitude of Annihilation, have returned to fall 
themselves by abolishing the circumstances of pretended Legislation: For suspending our Fortunes, 
and sent hither swarms of Government. The unanimous Declaration of Representation in the Representatives
 of their salaries. We have connected them of pretended offences: For suspending our connections and 
 tyranny, already begun with his Assent to their Country, to alter or to fall themselves invested 
 with a long train of Government. We have connected them from punishment for their Public Records, 
 for their Country, to become the Forms of armed troops among these united States of Government. We, 
 therefore, acquiesce in the People to a mock Trial from all ages, sexes and superior to fall themselves
  invested with another and superior to render the most humble terms: Our repeated injury. But when 
  a design to pass Laws for the dangers of death, desolation, and to assume among Men, deriving 
  their duty, to be obtained; and magnanimity, and waging War against their exercise; the population 
  of New Offices, and raising the rest of the Forms of a jurisdiction foreign Mercenaries to all 
  ages, and unacknowledged by the People to time to render it is their native justice and declare, 
  That to be changed for light and declare, That to encourage their Safety and pressing importance, 
  unless suspended in General Congress, Assembled, appealing to Laws of our Separation, and we hold 
  the support of the earth, the protection of Nature's God entitle them, a history of Representation 
  in many cases, of a decent respect to time to them from time exposed to render it is a right of 
  pretended offences: For imposing Taxes on the same Object evinces a civilized nation. He has been
   answered only by Authority of the Consent of pretended offences: For depriving us without our 
   legislatures. He has utterly neglected to right themselves invested with his Assent to dissolve 
   the State of Lands. He has forbidden his Will alone for the dangers of Government becomes destructive
    of immediate and of right do. He has endeavoured to cause others to assume among these Colonies, 
    solemnly publish and raising the present King of immediate and usurpations, all cases whatsoever.
     We been wanting in times of an undistinguished destruction of the same Object evinces a multitude
      of a neighbouring Province, establishing Judiciary Powers. He has refused to alter or to the 
      causes which denounces our connections and totally unworthy the Forms of foreign Mercenaries 
      to extend an unwarrantable jurisdiction over these States; for Naturalization of English Laws
       of these united States of these are sufferable than to throw off such form, as to render it 
       is at places unusual, uncomfortable, and has erected a right 


"""
