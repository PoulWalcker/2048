import random
from copy import deepcopy

def pretty_print(field):
    """ Print the nested list as a string with spacec between elements"""
    print('-' * 10)
    for row in field:
        print(*row)
    print('-' * 10)


def get_num_from_index(i, j):
    """Get number from row and column element from matrix"""
    return i * 4 + j + 1


def get_index_from_number(num):
    """ Get col and row numbers from element number from matrix"""
    num -= 1
    x, y = num // 4, num % 4
    return x, y


def insert_2_or_4(filed, x, y):
    """Insert 2 or 4 in matrix based on random function"""
    if random.random() < 0.75:
        filed[x][y] = 2
    else:
        filed[x][y] = 4
    return filed


def get_empy_list(field):
    """Get list of numbers of empty elements for matrix"""
    empty = list()
    for i in range(4):
        for j in range(4):
            if field[i][j] == 0:
                num = get_num_from_index(i, j)
                empty.append(num)
    return empty


def is_matrix_empty(field):
    """Check weather matrix empty or not"""
    for row in field:
        if 0 in row:
            return True
    return False

def move_left(field):
    """Move all elements to the left side of matrix"""
    origin = deepcopy(field)
    delta = 0
    for row in field:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(4):
        for j in range(3):
            if field[i][j] == field[i][j + 1] and field[i][j] != 0:
                field[i][j] *= 2
                delta += field[i][j]
                field[i].pop(j + 1)
                field[i].append(0)
    return field, delta, not field == origin


def move_right(field):
    """Move all elements to the right side of matrix"""
    origin = deepcopy(field)
    delta = 0
    for row in field:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0, 0)
    for i in range(4):
        for j in range(3, 0, -1):
            if field[i][j] == field[i][j - 1] and field[i][j] != 0:
                field[i][j] *= 2
                delta += field[i][j]
                field[i].pop(j - 1)
                field[i].insert(0, 0)
    return field, delta, not origin == field


def move_up(field):
    """Move all elements to the upper side of matrix"""
    origin = deepcopy(field)
    delta = 0
    for j in range(4):
        col = []
        for i in range(4):
            if field[i][j] != 0:
                col.append(field[i][j])
        while len(col) != 4:
            col.append(0)
        for i in range(3):
            if col[i] == col[i + 1] and col[i] != 0:
                col[i] *= 2
                delta += col[i]
                col.pop(i + 1)
                col.append(0)
        for i in range(4):
            field[i][j] = col[i]

    return field, delta, not origin == field


def move_down(field):
    """Move all elements to the bottom side of matrix"""
    origin = deepcopy(field)
    delta = 0
    for j in range(4):
        col = []
        for i in range(4):
            if field[i][j] != 0:
                col.append(field[i][j])
        while len(col) != 4:
            col.insert(0, 0)
        for i in range(3, 0, -1):
            if col[i] == col[i - 1] and col[i] != 0:
                col[i] *= 2
                delta += col[i]
                col.pop(i - 1)
                col.insert(0, 0)
        for i in range(4):
            field[i][j] = col[i]

    return field, delta, not origin == field


def can_move(field):
    for i in range(3):
        for j in range(3):
            if field[i][j] == field[i][j + 1] or field[i][j] == field[i + 1][j]:
                return True
    for i in range(1, 4):
        for j in range(1, 4):
            if field[i][j] == field[i - 1][j] or field[i][j] == field[i][j - 1]:
                return True
    return False
