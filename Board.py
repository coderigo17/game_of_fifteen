from random import shuffle

CEIL = 17
WIDTH = 4
HEIGHT = 4

class Board:
    """Models the board for our game"""

    def __init__(self):
        """Initializes the board"""

        self.board = [[1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12],
                        [13, 14, 15, "_"]]
        self.loc = [3, 3]

    def __repr__(self):
        """Renders the board on the screen"""

        print("\nWelcome to the game of fifteen!\n")
        for i in range(HEIGHT):
            for j in range(WIDTH):
                print(str(self.board[i][j]).rjust(2), end=" ")
            print()

        return ""

    def move(self, x, y):
        """General method for making a move"""
        if self.loc[0] + x < 0 or self.loc[0] + x > 3 or self.loc[1] + y < 0 or self.loc[1] + y > 3:
            return
        self.board[self.loc[0]][self.loc[1]], self.board[self.loc[0] + x][self.loc[1] + y] \
        = self.board[self.loc[0] + x][self.loc[1] + y], self.board[self.loc[0]][self.loc[1]]
        self.loc[0] += x
        self.loc[1] += y
        print("hello")

    def move_up(self):
        self.move(-1, 0)

    def move_right(self):
        self.move(0, 1)

    def move_down(self):
        self.move(1, 0)

    def move_left(self):
        self.move(0, -1)
