import unittest
from utils import get_num_from_index, get_empy_list, get_index_from_number, \
    is_matrix_empty, move_left, move_up, move_down, can_move

class Test_2048(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_num_from_index(1,2), 7)

    def test_2(self):
        self.assertEqual(get_num_from_index(3,3), 16)

    def test_3(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        b = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

        self.assertEqual(get_empy_list(b), a)

    def test_4(self):
        a = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        b = [[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

        self.assertEqual(get_empy_list(b), a)

    def test_5(self):
        a = []
        b = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

        self.assertEqual(get_empy_list(b), a)

    def test_6(self):
        self.assertEqual(get_index_from_number(7), (1, 2))

    def test_7(self):
        self.assertEqual(get_index_from_number(16), (3, 3))

    def test_8(self):
        self.assertEqual(get_index_from_number(1), (0, 0))

    def test_9(self):
        matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

        self.assertEqual(is_matrix_empty(matrix), False)

    def test_10(self):
        matrix = [[1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

        self.assertEqual(is_matrix_empty(matrix), True)

    def test_11(self):
        matrix = [[1, 1, 0, 1], [1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1]]

        self.assertEqual(is_matrix_empty(matrix), True)

    def test_12(self):
        matrix = [[2, 2, 0, 0],
                  [0, 4, 4, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]
        ]

        res = [[4, 0, 0, 0],
               [8, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]
        ]
        self.assertEqual(move_left(matrix), (res, 12))

    def test_13(self):
        matrix = [[2, 4, 4, 2],
                  [4, 0, 0, 2],
                  [0, 0, 0, 0],
                  [8, 8, 4, 4]
        ]

        res = [[2, 8, 2, 0],
               [4, 2, 0, 0],
               [0, 0, 0, 0],
               [16, 8, 0, 0]
        ]
        self.assertEqual(move_left(matrix), (res, 32))

    def test_14(self):
        matrix = [[2, 4, 0, 2],
                  [2, 0, 2, 0],
                  [4, 0, 2, 4],
                  [4, 4, 0, 0]
        ]

        res = [[4, 8, 4, 2],
               [8, 0, 0, 4],
               [0, 0, 0, 0],
               [0, 0, 0, 0]
        ]
        self.assertEqual(move_up(matrix), (res, 24))

    def test_15(self):
        matrix = [[2, 4, 0, 2],
                  [2, 0, 2, 0],
                  [4, 0, 2, 4],
                  [4, 4, 0, 0]
                  ]

        res = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [4, 0, 0, 2],
               [8, 8, 4, 4]
               ]
        self.assertEqual(move_down(matrix), (res, 24))

    def test_16(self):
        matrix = [[2, 4, 0, 2],
                  [2, 0, 2, 0],
                  [4, 0, 2, 4],
                  [4, 4, 0, 0]
                  ]

        self.assertEqual(can_move(matrix), True)

    def test_17(self):
        matrix = [[1, 4, 5, 2],
                  [3, 7, 9, 10],
                  [43, 66, 252, 41],
                  [445, 664, 20, 1110]
                  ]

        self.assertEqual(can_move(matrix), False)


