import sys
from utils import *
import pygame
from database import get_best, insert_result
import json
import os

# Board & PyGame data
GAMERS_DB = get_best()
BLOCK = 4
BLOCK_SIZE = 110
MARGIN = 10
W = BLOCK * BLOCK_SIZE + (BLOCK + 1) * MARGIN
H = W + BLOCK_SIZE
TITLE_REC = pygame.Rect(0, 0, W, BLOCK_SIZE)
score = None
username = None
matrix = None
path = os.getcwd()


def init_const():
    global score, matrix
    matrix = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    empty_list = get_empy_list(matrix)
    random.shuffle(empty_list)
    random_num1 = empty_list.pop()
    random_num2 = empty_list.pop()
    x1, y1 = get_index_from_number(random_num1)
    x2, y2 = get_index_from_number(random_num2)
    matrix = insert_2_or_4(matrix, x1, y1)
    matrix = insert_2_or_4(matrix, x2, y2)
    score = 0


if 'data.txt' in os.listdir(path):
    with open('resources/data.txt') as file:
        data = json.load(file)
        matrix = data['matrix']
        username = data['username']
        score = data['score']
    full_path = os.path.join(path, 'data.txt')
    os.remove(full_path)
else:
    init_const()

# Colors
WHITE = (255, 255, 255)
WHITE_PALE = (255, 255, 128)
WHITE_PALE_STRONG = (255, 255, 0)
GRAY = (130, 130, 130)
BLACK = (0, 0, 0)
BLUE = (235, 255, 255)
BLUE_LIGHT = (235, 255, 128)
BLUE_WHITE = (235, 255, 0)
BLUE_WHITE_2X = (235, 255, 10)
YELLOW = (255, 255, 102)
ORANGE = (255, 165, 0)
RED = (255, 69, 0)
PURPLE = (128, 0, 128)

COLORS = {
    0: GRAY,
    2: WHITE,
    4: WHITE_PALE,
    8: WHITE_PALE_STRONG,
    16: BLUE,
    32: BLUE_LIGHT,
    64: BLUE_WHITE,
    128: BLUE_WHITE_2X,
    256: YELLOW,
    512: ORANGE,
    1024: RED,
    2048: PURPLE,
}

# Init PyGame & Board
pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('2048')


def draw_top_gamers():
    font_top = pygame.font.SysFont('simsun', 30)
    font_gamer = pygame.font.SysFont('simsun', 24)
    text_head = font_top.render('Best tries: ', True, BLACK)
    screen.blit(text_head, (250, 10))
    for index, gamer in enumerate(GAMERS_DB):
        name, game_score = gamer
        s = f'{index + 1}. {name}: {game_score}'
        text_gamer = font_gamer.render(s, True, BLACK)
        screen.blit(text_gamer, (250, 35 + 20 * index))


def draw_interface(game_score, delta=0):
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    font = pygame.font.SysFont('stxingkai', 70)
    font_score = pygame.font.SysFont('simsun', 48)
    font_delta = pygame.font.SysFont('simsun', 32)
    score_title = font_score.render('Score: ', True, BLACK)
    score_val = font_score.render(f'{game_score}', True, BLACK)
    screen.blit(score_title, (20, 35))
    screen.blit(score_val, (175, 35))
    if delta > 0:
        delta_val = font_delta.render(f'+{delta}', True, BLUE_WHITE)
        screen.blit(delta_val, (170, 65))
    pretty_print(matrix)
    draw_top_gamers()
    for row in range(BLOCK):
        for col in range(BLOCK):
            val = matrix[row][col]
            text = font.render(f'{val}', True, BLACK)
            w = col * BLOCK_SIZE + (col + 1) * MARGIN
            h = row * BLOCK_SIZE + (row + 1) * MARGIN + BLOCK_SIZE
            pygame.draw.rect(screen, COLORS[val], (w, h, BLOCK_SIZE, BLOCK_SIZE))
            if val != 0:
                font_w, font_h = text.get_size()
                text_x = w + (BLOCK_SIZE - font_w) // 2
                text_y = h + (BLOCK_SIZE - font_h) // 2
                screen.blit(text, (text_x, text_y))


def draw_intro():
    global username
    img = pygame.image.load('resources/2048.png')
    font = pygame.font.SysFont('stxingkai', 70)
    font_welcome = font.render('Welcome', True, WHITE)
    name = 'Enter name'
    is_name_found = False

    while not is_name_found:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name == 'Enter name':
                        name = event.unicode
                    else:
                        name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(name) > 2 and name != 'Enter name':
                        username = name
                        is_name_found = True
                        break
        screen.fill(BLACK)
        text_name = font.render(name, True, WHITE)
        rect_name = text_name.get_rect()
        rect_name.center = screen.get_rect().center

        screen.blit(pygame.transform.scale(img, [200, 200]), [10,10])
        screen.blit(font_welcome, [230, 80])
        screen.blit(text_name, rect_name)
        pygame.display.update()
    screen.fill(BLACK)


def draw_game_over():
    global username, matrix, score, GAMERS_DB
    img = pygame.image.load('resources/2048.png')
    font = pygame.font.SysFont('stxingkai', 65)
    text_game_over = font.render('Game over', True, WHITE)
    text_score = font.render(f'Score: {score}', True, WHITE)
    best_score = GAMERS_DB[0][1]

    if score > best_score:
        text = 'New Record'
    else:
        text = f'Record {best_score}'
    text_record = font.render(text, True, WHITE)
    insert_result(username, score)
    GAMERS_DB = get_best()
    did_started_again = False
    while not did_started_again:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    did_started_again = True
                    init_const()
                elif event.key == pygame.K_RETURN:
                    username = None
                    did_started_again = True
                    init_const()

        screen.fill(BLACK)
        screen.blit(text_game_over, (220, 80))
        screen.blit(text_record, (30, 300))
        screen.blit(pygame.transform.scale(img, [200, 200]), [10,10])
        screen.blit(text_score, (30, 250))
        pygame.display.update()
    screen.fill(BLACK)


def save_game():
    data = {
        'username': username,
        'score': score,
        'matrix': matrix
    }
    with open('resources/data.txt', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile)


def game_loop():
    global score, matrix
    draw_interface(score)
    pygame.display.update()
    is_list_updated = False
    while is_matrix_empty(matrix) or can_move(matrix):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game()
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                delta = 0
                if event.key == pygame.K_LEFT:
                    matrix, delta, is_list_updated = move_left(matrix)
                elif event.key == pygame.K_RIGHT:
                    matrix, delta, is_list_updated = move_right(matrix)
                elif event.key == pygame.K_UP:
                    matrix, delta, is_list_updated = move_up(matrix)
                elif event.key == pygame.K_DOWN:
                    matrix, delt, is_list_updated = move_down(matrix)
                # input()
                score += delta
                if is_matrix_empty(matrix) and is_list_updated:
                    empty_list = get_empy_list(matrix)
                    random.shuffle(empty_list)
                    random_num = empty_list.pop()
                    x, y = get_index_from_number(random_num)
                    print(f'We have filled element by number {random_num}')
                    board = insert_2_or_4(matrix, x, y)
                    is_list_updated = False
                draw_interface(score, delta)
                pygame.display.update()

init_const()

while True:
    if username is None:
        draw_intro()
    else:
        game_loop()
        draw_game_over()
