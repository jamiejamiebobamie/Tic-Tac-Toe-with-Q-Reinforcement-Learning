# Design a Tic-tac-toe game that is played between two players on a n x n grid.
#
# You may assume the following rules:
#
# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves is allowed.
# A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
# Example:
# Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.
#
# TicTacToe toe = new TicTacToe(3);
#
# toe.move(0, 0, 1); -> Returns 0 (no one wins)
# |X| | |
# | | | | // Player 1 makes a move at (0, 0).
# | | | |
#
# toe.move(0, 2, 2); -> Returns 0 (no one wins)
# |X| |O|
# | | | | // Player 2 makes a move at (0, 2).
# | | | |
#
# toe.move(2, 2, 1); -> Returns 0 (no one wins)
# |X| |O|
# | | | | // Player 1 makes a move at (2, 2).
# | | |X|
#
# toe.move(1, 1, 2); -> Returns 0 (no one wins)
# |X| |O|
# | |O| | // Player 2 makes a move at (1, 1).
# | | |X|
#
# toe.move(2, 0, 1); -> Returns 0 (no one wins)
# |X| |O|
# | |O| | // Player 1 makes a move at (2, 0).
# |X| |X|
#
# toe.move(1, 0, 2); -> Returns 0 (no one wins)
# |X| |O|
# |O|O| | // Player 2 makes a move at (1, 0).
# |X| |X|
#
# toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
# |X| |O|
# |O|O| | // Player 1 makes a move at (2, 1).
# |X|X|X|
# Follow up:
# Could you do better than O(n2) per move() operation?
#
# Hint:
#
# Could you trade extra space such that move() operation can be done in O(1)?
# You need two arrays: int rows[n], int cols[n], plus two variables: diagonal, anti_diagonal.

"""
no one cheats in this game so we don't need to keep track of if the move is valid
    only if there's a winner or if all squares have been filled.

the key insight is that we don't need to worry about a row, column, or diagonal the moment
    it contains both an X and O, because it can't be a winner. (must span 'n' to win.)

make bins out of all rows, columns, and  diagonals. ("bin" = dictionary)

each square has an i,j index.

rows have repeat i's
    (a row's key would be i)
columns have repeat j's
    (a column's key would be j)

          O X O X
          X O X X
          O X O O
          X O O O

     (0,0)(1,1)(2,2)(3,3)
     (0,3)(1,2)(2,1)(3,0)

            O X
            X O

    (0,0)(1,1)
    (0,1)(1,0)

     the indices of a diagonal either
     add up to equal n-1 (i + j == n - 1)
     or they equal each other (i == j)
     depending on whether it's going from
     left to right (i == j)
     or
     right to left (i + j == n - 1)

"""
import sys
import random as rand

class TicTacToe:
    def __init__(self, n=3):
        self.n = n
        self.go = "Tie" # The object that is returned when the game is over.

        # the bins
        self.rows = {}
        self.cols = {}
        self.diags = {'step': [True, "", 0], 'same': [True, "", 0]}

        # an array of i-j board indices
        self.board = self.buildBoard(n)

        # an array of randomized i-j board indices
        self.order = self.randomOrder(self.board)

    def buildBoard(self, n):
        """Returns an array of (i,j) index keys to be randomized.
        Adds keys to the rows and cols dictionaries."""

        boardDict = []
        diagCount = 0

        for i in range(n):
            self.rows[i] = [True, "", 0] #homogenous, X/O, count of X's/O's
            self.cols[i] = [True, "", 0]
            for j in range(n):

# Is there a faster way to make this array than nested for loops?
                boardDict.append((i,j))
        return boardDict

    def randomOrder(self, array):
        """Takes a dictionary of index-keys and mixes up their order.
        Returns an array of i-j index-keys. This is the order the tiles will be played.
        X will play even tiles starting at 0 and O will play odd starting at 1."""

        iter = 0
        order = array
        for key in array:
            rando = rand.randint(iter,len(order)-1)
            order[rando], order[iter] = order[iter], order[rando]
            iter += 1
        return order

    def play(self):
        """Plugs the self.order values into the respective dictionaries.
        Game ends when the count of one of the dictionaries == the board size
        or if all squares have been filled."""

        value = 0 #player dictionary key
        player = {0: 'O', 1: 'X'}

        moveCount = 0 #how many moves have occurred. also doubles as the self.order index.
        turn = ""
        while moveCount < self.n**2 and self.go == "Tie":
            value = not value
            turn = player[value] #X starts
            key = self.order[moveCount]
            i = key[0]
            j = key[1]


# self.rows[i][0] == homogenous?
# self.rows[i][1] == X/O?
# self.rows[i][2] == count of X's/O's?

# Check to see if row i is 'homogenous' (contains only X's or O's):
            if self.rows[i][0]:

# Check to see if any square in row i has been played. If it has been played,
# check to see if it was the same person who's current turn it is.
                if self.rows[i][1] == "" or player[value] == self.rows[i][1]:

# Mark the column with the current person's token (X or O).
# Admittedly, this could be improved to not update every time.
                    self.rows[i][1] = turn

# Update the count by one.
                    self.rows[i][2] += 1

# If the count is equal to the board size, end the game and return who won and how.
                    if self.rows[i][2] == self.n:
                        self.go = (turn, 'row ' + str(i))

# If the current person who's turn it is,
# is not the same as the previous player who played this row,
# set this row's 'homogenous' attribute to false.
                else:
                    self.rows[i][0] = False

            if self.cols[j][0]:
                if self.cols[j][1] == "" or player[value] == self.cols[j][1]:
                    self.cols[j][1] = turn
                    self.cols[j][2] += 1
                    if self.cols[j][2] == self.n:
                        self.go = (turn, 'column ' + str(j))
                else:
                    self.cols[j][0] = False

# On boards of odd-sized 'n' (n = 3,5,7,etc...)
# the middle square is part of both diagonals: 'step' and 'same':
            if i == j:
                if self.diags['same'][0]:
                    if self.diags['same'][1] == "" or player[value] == self.diags['same'][1]:
                        self.diags['same'][1] = turn
                        self.diags['same'][2] += 1
                        if self.diags['same'][2] == self.n:
                            self.go = (turn, 'diagonal from 0,0 to n-1,n-1')
                    else:
                        self.diags['same'][0] = False

            if i + j + 1 == self.n:
                if self.diags['step'][0]:
                    if self.diags['step'][1] == "" or player[value] == self.diags['step'][1]:
                        self.diags['step'][1] = turn
                        self.diags['step'][2] += 1
                        if self.diags['step'][2] == self.n:
                            self.go = (turn, 'diagonal from n-1,0 to 0,n-1')
                    else:
                        self.diags['step'][0] = False

            moveCount += 1
            print(turn, key)
        else:
            return self.go

if __name__ == "__main__":
    n = int(sys.argv[1])
    new = TicTacToe(n)
    print(new.play())


# INPUT: python3 tictactoe3.py

# OUTPUT:
# ('X', (0, 0))
# ('O', (1, 0))
# ('X', (1, 1))
# ('O', (3, 2))
# ('X', (0, 2))
# ('O', (3, 1))
# ('X', (3, 0))
# ('O', (0, 3))
# ('X', (3, 3))
# ('O', (1, 3))
# ('X', (0, 1))
# ('O', (2, 0))
# ('X', (2, 2))
# ('X', 'diagonal from left to right')
# [Finished in 0.065s]

     #     X X X O
     #     O X _ O
     #     O _ X _
     #     X O O X
