# -*- coding:utf8 -*-

from matrix import *

class Action:
    def __init__(self):
        pass

    def move(self, event, matrix):
        if event == 258:
            self.move_down(matrix)
        elif event == 259:
            self.move_up(matrix)
        elif event == 260:
            self.move_left(matrix)
        elif event == 261:
            self.move_right(matrix)

    def move_left(self, matrix):
        status = matrix.status
        for line in status:
            items = filter(lambda x: x != 0, line)
            for i in range(len(line)):
                line[i] = items[i] if i < len(items) else 0
            if line[1] == line[0] and line[3] == line[2]:
                line[0] += line[1]
                line[1] = 0
                line[2] += line[3]
                line[3] = 0
            for i in range(1,len(line)):
                if line[i] == line[i - 1]:
                    line[i - 1] += line[i]
                    line[i] = 0
                    break

            items = filter(lambda x: x != 0, line)
            for i in range(len(line)):
                line[i] = items[i] if i < len(items) else 0

    def move_right(self, matrix): 
        status = matrix.status
        for line in status:
            items = filter(lambda x: x != 0, line)
            for i in range(1, len(line) + 1):
                line[-i] = items[-i] if i < len(items) + 1 else 0
            if line[0] == line[1] and line[2] == line[3]:
                line[3] += line[2]
                line[2] = 0
                line[1] += line[0]
                line[0] = 0
            for i in range(len(line) -1):
                if line[i] == 0:continue
                if line[i] == line[i + 1]:
                    line[i + 1] += line[i]
                    line[i] = 0
                    break
            items = filter(lambda x:x != 0, line)
            for i in range(1, len(line) + 1):
                line[-i] = items[-i] if i < len(items) + 1 else 0

    def move_up(self, matrix):
        status = matrix.status
        for c in range(matrix.width):
            items = []
            for r in range(matrix.height):
                if status[r][c] != 0:
                    items.append(status[r][c])
            for r in range(matrix.height):
                status[r][c] = items[r] if r < len(items) else 0
            if status[1][c] == status[0][c] and status[3][c] == status[2][c]:
                status[0][c] += status[1][c]
                status[2][c] += status[3][c]
                status[1][c] = 0
                status[3][c] = 0
            for r in range(1, matrix.height):
                if status[r][c] == 0:continue
                if status[r][c] == status[r - 1][c]:
                    status[r -1][c] += status[r][c]
                    status[r][c] = 0
                    break
            items = []
            for r in range(matrix.height):
                if status[r][c] != 0:
                    items.append(status[r][c])
            for r in range(matrix.height):
                status[r][c] = items[r] if r < len(items) else 0

    def move_down(self, matrix):
        status = matrix.status
        for c in range(matrix.width):
            items = []
            for r in range(matrix.height):
                if status[r][c] != 0:
                    items.append(status[r][c])
            for r in range(1, matrix.height + 1):
                status[-r][c] = items[-r] if r < len(items) + 1 else 0
            if status[1][c] == status[0][c] and status[3][c] == status[2][c]:
                status[1][c] += status[0][c]
                status[3][c] += status[2][c]
                status[0][c] = 0
                status[2][c] = 0
            for r in range(matrix.height - 1):
                if status[r][c] == 0:continue
                if status[r][c] == status[r + 1][c]:
                    status[r + 1][c] += status[r][c]
                    status[r][c] = 0
                    break
            items = []
            for r in range(matrix.height):
                if status[r][c] != 0:
                    items.append(status[r][c])
            for r in range(1, matrix.height + 1):
                status[-r][c] = items[-r] if r < len(items) + 1 else 0

if __name__ == '__main__':
    m = Matrix()
    m.prepare()

    def show(m):
        for line in m.status:
            print(line)
        print('-----------')
    
    a = Action()
    a.move_up(m)
    show(m)
    a.move_right(m)
    show(m)
    a.move_down(m)
    show(m)
    a.move_left(m)
    show(m)
