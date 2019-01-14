from random import shuffle

CEIL = 17
WIDTH = 4
HEIGHT = 4

class Board:
    """Models the board for our game"""

    def __init__(self):
        self.solved = [["1", "2", "3", "4"],
                        ["5", "6", "7", "8"],
                        ["9", "10", "11", "12"],
                        ["13", "14", "15", "_"]]
        self.loc = [3, 3]

    def __repr__(self):
        print("\nWelcome to the game of fifteen!\n")
        for i in range(HEIGHT):
            for j in range(WIDTH):
                print(self.solved[i][j].rjust(2), end=" ")
            print()

        return ""
