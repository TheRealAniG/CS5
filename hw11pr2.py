import random

def inarow_Neast(ch, r_start, c_start, A, N):
    """This should start from r_start and c_start and check for N-in-a-row eastward of element ch, returning True or False, as appropriate.
    """
    num_rows = len(A)      # Number of rows is len(A)
    num_cols = len(A[0])   # Number of columns is len(A[0])

    if r_start < 0 or r_start > num_rows:
        return False       # Out of bounds in rows

    # Other out-of-bounds checks...
    if c_start < 0 or c_start > num_cols - N:
        return False       # Out of bounds in columns

    # Are all of the data elements correct?
    for i in range(N):                  # Loop index i as needed
        if A[r_start][c_start+i] != ch: # Check for mismatches
            return False                # Mismatch found--return False

    return True                         # Loop found no mismatches--return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """This should start from r_start and c_start and check for N-in-a-row southward of element ch, returning True or False, as appropriate.
    """
    num_rows = len(A)      # Number of rows is len(A)
    num_cols = len(A[0])   # Number of columns is len(A[0])

    if r_start < 0 or r_start > num_rows - N:
        return False       # Out of bounds in rows

    # Other out-of-bounds checks...
    if c_start < 0 or c_start > num_cols:
        return False       # Out of bounds in columns

    # Are all of the data elements correct?
    for i in range(N):                  # Loop index i as needed
        if A[r_start+i][c_start] != ch: # Check for mismatches
            return False                # Mismatch found--return False

    return True                         # Loop found no mismatches--return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """This should start from r_start and c_start and check for N-in-a-row southeastward of element ch, returning True or False, as appropriate.
    """
    num_rows = len(A)      # Number of rows is len(A)
    num_cols = len(A[0])   # Number of columns is len(A[0])

    if r_start < 0 or r_start > num_rows - N:
        return False       # Out of bounds in rows

    # Other out-of-bounds checks...
    if c_start < 0 or c_start > num_cols - N:
        return False       # Out of bounds in columns

    # Are all of the data elements correct?
    for i in range(N):                  # Loop index i as needed
        if A[r_start+i][c_start+i] != ch: # Check for mismatches
            return False                # Mismatch found--return False

    return True                         # Loop found no mismatches--return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """This should start from r_start and c_start and check for N-in-a-row northeastward of element ch, returning True or False, as appropriate.
    """
    num_rows = len(A)      # Number of rows is len(A)
    num_cols = len(A[0])   # Number of columns is len(A[0])

    if r_start < 0 or r_start > num_rows + N:
        return False       # Out of bounds in rows

    # Other out-of-bounds checks...
    if c_start < 0 or c_start > num_cols - N:
        return False       # Out of bounds in columns

    # Are all of the data elements correct?
    for i in range(N):                  # Loop index i as needed
        if A[r_start - i][c_start+i] != ch: # Check for mismatches
            return False                # Mismatch found--return False

    return True                         # Loop found no mismatches--return True


class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # The string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-' + "\n"   # Bottom of the board
        for x in range(self.width):
                s += " " + str(round((x % 10),0))
        # Add code here to put the numbers underneath

        return s       # The board is complete; return it
    
    def addMove(self, col, ox):
         """This method takes two arguments: the first, col, represents the index of the column
           to which the checker will be added. The second argument, ox, is a 1-character string 
           representing the checker to add to the board.
         """
         for x in range(self.height):
            if(self.data[self.height - x - 1][col] == " "):
                self.data[self.height - x - 1][col] = ox
                break
              
    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'

    
    def clear(self):
         """clears the board"""
         self.data = [[' ']*self.width for row in range(self.height)]

    def allowsMove(self, c):
        """checks if a move is allowed in column C
        """

        if(c < 0):
            return False
        elif(c > self.width - 1):
            return False
        elif(self.data[0][c] != " "):
            return False
        return True

    def isFull(self):
        """checks if the board is full. True if it is, False if its not
        """
        
        for x in range(self.width):
             if(self.allowsMove(x)):
                  return False
        return True
    
    def delMove(self, c):
        """Removes a checker from column c, does nothing if no checkers
        """
        for x in range(self.height):
              if(self.data[x][c] != " "):
                   self.data[x][c] = " "
                   break
              
    def winsFor(self, ox): 
        """Checks if there are four checkers of type of ox in a row on the board.
            True if there are, False if there are not
        """
        H = self.height
        W = self.width
        D = self.data

        # Check to see if ox wins, starting from any checker:
        for row in range(H):
            for col in range(W):
                if inarow_Neast(ox, row, col, D, 4) == True:
                    return True
                elif inarow_Nnortheast(ox, row, col, D, 4) == True:
                    return True
                elif inarow_Nsouth(ox, row, col, D, 4) == True:
                    return True
                elif inarow_Nsoutheast(ox, row, col, D, 4) == True:
                    return True
                # you need three more, very similar, such checks
                # for the three other directions!

        # but, if it looks at EACH row and col and never finds a win...
        return False     # only gets here if it never returned True, above
    
    def hostGame(self):
        """Runs a whole game of connect 4. X goes first"""
        turn = "X"
        print("Welcome to Connect 4! \n")
        while True:
            print(self)
            user_column = -1    # intentionally not valid!

            if(turn == "X"):
                while self.allowsMove(user_column) == False:
                    # intentionally not valid, the first time...
                    user_string = input("{0}'s Choice:   ".format(turn))
                    try:
                        user_column = int(user_string)
                    except ValueError:       # in case an integer wasn't typed...
                        user_column = -1
            else:
                user_column = self.aiMove("O")
            self.addMove(user_column, turn)

            print(self)

            if(self.winsFor("X")):
                print("X wins!")
                break
            elif(self.winsFor("O")):
                print("O wins!")
                break
            elif(self.isFull()):
                print("The board is full it is a draw")
                break
                
            if(turn == "X"):
                turn = "O"
            else:
                turn = "X"

    def colsToWin(self, ox):
        """ox is either the string X or O
           returns the list of possible columns where ox can win on the next turn
        """
        wins = []
        for col in range(0, self.width):
            if(self.allowsMove(col)):
                self.addMove(col, ox)
                if(self.winsFor(ox)):
                    wins += [col]
                self.delMove(col)
        return wins

    def aiMove(self, ox):
        """Ox is either a string X or O
           returns a string of where to make a move, that wins when it can, blocks a win when it can,
           otherwise returns a random column
        """
        ai = ox
        player = "X"
        if(ai == "X"):
            player = "O"
        aiWins = self.colsToWin(ai)
        playerWins = self.colsToWin(player)

        if(len(aiWins)>0):
            return aiWins[0]
        elif(len(playerWins) > 0):
            return playerWins[0]
        else:
            return random.randint(0, self.width-1)

