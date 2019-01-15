from copy import deepcopy
from os import system
from random import randint, seed

MAX_COL = 4
MAX_ROW = 4
SHUFFLE_MAGNITUDE = 10000

class Board:
    """Models the board for our game"""

    def __init__(self):
        """Initializes the board"""

        # The solved board
        self.goal = [[" 1", " 2", " 3", " 4"],
                        [" 5", " 6", " 7", " 8"],
                        [" 9", "10", "11", "12"],
                        ["13", "14", "15", "__"]]

        # The "current" board; we will randomize it using legal moves
        self.board = deepcopy(self.goal)

        # The location of the empty space [row_index, column_index]; [3,3] by default
        self.loc = [MAX_ROW - 1, MAX_COL - 1]

        # Map of moves by index (useful for randomization)
        self.moves = {0: self.move_up, 1: self.move_right, 2: self.move_down, 3: self.move_left}

    def __repr__(self):
        """Renders the board on the screen"""

        print("Welcome to the game of fifteen!\n")
        for i in range(MAX_ROW):
            for j in range(MAX_COL):
                print(self.board[i][j], end=" ")
            print()

        # __repr__ MUST return a string
        return ""

    def move(self, x, y):
        """General method for making a move"""

        # Prevent user from moving beyond edge of the board
        if self.loc[0] + x < 0 or self.loc[0] + x > 3 or self.loc[1] + y < 0 or self.loc[1] + y > 3:
            return

        # For a legal move, swap the location of the empty space with that of the adjacent number
        self.board[self.loc[0]][self.loc[1]], self.board[self.loc[0] + x][self.loc[1] + y] \
        = self.board[self.loc[0] + x][self.loc[1] + y], self.board[self.loc[0]][self.loc[1]]

        # Update the location of the empty space
        self.loc[0] += x
        self.loc[1] += y

    # Make moves by adding/subtracting 1 to corresponding empty space location index
    def move_up(self):
        self.move(-1, 0)

    def move_right(self):
        self.move(0, 1)

    def move_down(self):
        self.move(1, 0)

    def move_left(self):
        self.move(0, -1)

    def refresh(self, beginning=False):
        """Clears screen, prints board, checks if game is over"""

        system("clear")
        print(self)
        if not beginning and self.goal == self.board:
            print("Congrats! You won! ")
            return False

        return True

    def shuffle(self):
        """Randomizes the board using a succession of legal moves from a solved state"""

        # Do some number of random moves
        seed()
        for i in range(SHUFFLE_MAGNITUDE):
            m = randint(0, 3)
            self.moves[m]()

        # Optionally move the empty space to the lower right corner
        for i in range(MAX_COL):
            self.moves[2]()
        for i in range(MAX_ROW):
            self.moves[1]()

    def solve(self):
        """Solves the game"""
        self.board = deepcopy(self.goal)
