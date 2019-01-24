from pynput import keyboard
from time import sleep

from Board import Board

# Create game board
b = Board()

def main():
    # Randomize board and update display on screen to show board
    b.shuffle()
    b.refresh()

    # https://pypi.org/project/pynput/
    # Collect events until released (cancel by returning False from on_press or on_release)
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def on_press(key):
    """Behavior executed immediately on keypress"""

    # Update display on screen to hide terminal echo
    b.refresh()

def on_release(key):
    """Behavior executed on key release"""

    # Escape key quits the game
    if key == keyboard.Key.esc:
        return False

    # User can make moves using the arrow keys
    elif key == keyboard.Key.up:
        b.board, b.loc = b.move_up(b.board, b.loc)
    elif key == keyboard.Key.right:
        b.board, b.loc = b.move_right(b.board, b.loc)
    elif key == keyboard.Key.down:
        b.board, b.loc = b.move_down(b.board, b.loc)
    elif key == keyboard.Key.left:
        b.board, b.loc = b.move_left(b.board, b.loc)

    # Shift key solves the game and quits
    elif key == keyboard.Key.shift:
        print("Thinking...")
        sleep(1)
        moves = b.solve()
        persist = True
        for m in moves:
            b.moves[m](b.board, b.loc)
            persist = b.refresh()
            sleep(1)
        return persist

    # Update display on screen to show board after most recent move
    return b.refresh()


if __name__ == '__main__':
    main()
