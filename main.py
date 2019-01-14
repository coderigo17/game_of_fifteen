from pynput import keyboard

from Board import Board
from helpers import refresh

b = Board()

def main():
    refresh(b)

    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

def on_press(key):
    refresh(b)

def on_release(key):
    if key == keyboard.Key.up:
        b.move_up()
    elif key == keyboard.Key.right:
        b.move_right()
    elif key == keyboard.Key.down:
        b.move_down()
    elif key == keyboard.Key.left:
        b.move_left()
    elif key == keyboard.Key.esc:
        # Stop listener
        return False
    refresh(b)

if __name__ == '__main__':
    main()
