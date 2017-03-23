# -*- coding:utf8 -*-
import curses
from matrix import *

# 绘制状态
class Render:
    def __init__(self):
        curses.use_default_colors()

    def show(self, screen, matrix):
        screen.clear()
        status = matrix.status
        for line in status:
            screen.addstr(' '.join(('%4d' % x) for x in line))
            screen.addstr('\n')


if __name__ == '__main__':
    def main(stdscr):
        class Matrix:
            def __init__(self):
                self.status = [
                    [1, 0, 0, 0], 
                    [0, 1, 0, 0], 
                    [0, 0, 1, 0], 
                    [0, 0, 0, 1],
                ]
        Render().show(stdscr, Matrix())
        key = stdscr.getch()

    curses.wrapper(main)
