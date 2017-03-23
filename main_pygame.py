import pygame
from pygame.locals import *
from action import *
from matrix import *
from render import *


def load_images_path():
    paths = {
        'bg': 'images/2048_bg.jpg',
        '0': 'images/0.jpg',
        }
    return paths


def render(status):
    start_x = 41
    start_y = 27
    blank_w = 14
    blank_h = 13
    block_w = 130
    block_h = 131
    step_w = blank_w + block_w
    step_h = blank_h + block_h
    for i in range(len(status)):
        y = start_y + i * step_h
        for j in range(len(status[i])):
            x = start_x + j * step_w
            origil = pygame.image.load('images/0.jpg')
            screen.blit(origil, (x, y))
            if status[i][j] != 0 and len(str(status[i][j])) == 1:
                text_screen_1 = my_font_1.render(str(status[i][j]), True, (255, 0, 0))
                screen.blit(text_screen_1, (x + 25, y + 6))
            if status[i][j] != 0 and len(str(status[i][j])) == 2:
                text_screen_2 = my_font_2.render(str(status[i][j]), True, (0, 255, 0))
                screen.blit(text_screen_2, (x, y + 13))
            if status[i][j] != 0 and len(str(status[i][j])) == 3:
                text_screen_3 = my_font_3.render(str(status[i][j]), True, (0, 0, 255))
                screen.blit(text_screen_3, (x, y + 30))
            if status[i][j] != 0 and len(str(status[i][j])) == 4:
                text_screen_4 = my_font_4.render(str(status[i][j]), True, (255, 255, 255))
                screen.blit(text_screen_4, (x, y + 45))


pygame.init()
screen = pygame.display.set_mode((640, 625), 0, 32)
pygame.display.set_caption('2048')
my_font = pygame.font.SysFont(None, 80)
my_font_1 = pygame.font.SysFont(None, 200)
my_font_2 = pygame.font.SysFont(None, 160)
my_font_3 = pygame.font.SysFont(None, 110)
my_font_4 = pygame.font.SysFont(None, 76)
background = pygame.image.load(load_images_path()['bg'])

matrix = Matrix()
matrix.prepare(2)

action = Action()


game_over = False
game_win = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif (not game_over) and (not game_win) and (event.type == pygame.KEYDOWN):
            if event.key == pygame.K_UP:
                action.move_up(matrix)
            elif event.key == pygame.K_DOWN:
                action.move_down(matrix)
            elif event.key == pygame.K_LEFT:
                action.move_left(matrix)
            elif event.key == pygame.K_RIGHT:
                action.move_right(matrix)
            matrix.next()
    game_over = True
    for i in range(matrix.height):
        for j in range(matrix.width):
            if matrix.status[i][j] == 0:
                game_over = False
            if matrix.status[i][j] == 2048:
                game_win = True
        
    screen.blit(background, (0, 0))

    render(matrix.status)

    if game_over:
        text_screen = my_font.render('Game  Over', True, (0, 0, 0))
        screen.blit(text_screen, (150, 280))
    if game_win:
        text_screen = my_font.render('Game  Win', True, (0, 0, 0))
        screen.blit(text_screen, (150, 280))
    pygame.display.update()
