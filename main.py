import curses
import pynput
import sys

def on_press(key: pynput.keyboard.Key):
    global x, y
    try:
        if key.char == 'q':
            return False
        if key.char == 'w' and y > 0:
            y -= 1
        elif key.char == 's' and y < MAX_Y-1:
            y += 1
        elif key.char == 'a' and x > 0:
            x -= 1
        elif key.char == 'd' and x < MAX_X-1:
            x += 1
        win.move(y+1, x+1)
        win.refresh()
    except AttributeError:
        pass

x = y = 0
MAX_X, MAX_Y = 20, 10
curses.initscr()
win = curses.newwin(MAX_Y+2, MAX_X+2)
win.border()
win.move(1, 1)
win.refresh()
with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()
