# -*- coding:utf8 -*-

import random

class Matrix:
    def __init__(self, width = 4, height = 4):
        self.width = width
        self.height = height
        self.status = [([0] * width) for i in range(height)]

    def prepare(self, k = 2):
        location = random.sample(range(self.width * self.height), k)
        for loc in location:
            row = loc / self.width
            col = loc % self.width
            self.status[row][col] = 2

    def next(self):
        available = []
        for r in range(self.height):
            for c in range(self.width):
                if self.status[r][c] == 0:
                    available.append((r, c))
        loc = random.sample(available, 1)[0]
        self.status[loc[0]][loc[1]] = 2


if __name__ == '__main__':
    m = Matrix()
    m.prepare()
    print(m.status)
    m.next()
    print(m.status)
