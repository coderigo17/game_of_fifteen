from pynput import keyboard

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

    # Escape key solves the game and quits
    if key == keyboard.Key.esc:
        b.solve()
        return b.refresh()

    # User can make moves using the arrow keys
    elif key == keyboard.Key.up:
        b.move_up()
    elif key == keyboard.Key.right:
        b.move_right()
    elif key == keyboard.Key.down:
        b.move_down()
    elif key == keyboard.Key.left:
        b.move_left()

    # Update display on screen to show board after most recent move
    return b.refresh()


if __name__ == '__main__':
    main()
