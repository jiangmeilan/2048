import curses
from action import *
from matrix import *
from render import *

def main(stdscr):
    matrix = Matrix()
    action = Action()
    render = Render()
    matrix.prepare()
    render.show(stdscr, matrix)

    while True:
        key = stdscr.getch()
        if key == ord('q'): break
        action.move(key, matrix)
        matrix.next()
        render.show(stdscr, matrix)

curses.wrapper(main)

