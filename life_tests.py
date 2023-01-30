import unittest
from life import count_neighbours, check_cell

class LifeTest(unittest.TestCase):
    def test_count_neighbours(self):
        map = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0 ,0]
        ]
        neighbours = count_neighbours(map, 1, 1)
        self.assertEqual(neighbours, 0)
        map = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0 ,1]
        ]
        neighbours = count_neighbours(map, 1, 1)
        self.assertEqual(neighbours, 1)
        map = [
            [1, 0, 0],
            [0, 0, 0],
            [0, 0 ,1]
        ]
        neighbours = count_neighbours(map, 1, 1)
        self.assertEqual(neighbours, 2)
        
    def test_count_neighbours_on_border(self):
        # must count cells in (0, 1), (-1, 0), (1, 1), (0, 3), (3, 3)
        map = [
            [0, 1, 0, 0],
            [1, 0, 0, 1],
            [0, 0 ,0, 0],
            [0, 0 ,0, 1],
        ]
        neighbours = count_neighbours(map, 0, 0)
        self.assertEqual(neighbours, 4)
        map = [
            [0, 1, 0, 0],
            [1, 0, 0, 1],
            [0, 0 ,0, 0],
            [0, 0 ,0, 1],
        ]
        neighbours = count_neighbours(map, 1, 0)
        self.assertEqual(neighbours, 2)
        
    def test_rule_1(self):
        map = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0 ,0]   
        ]
        is_alive = check_cell(map, 1, 1)
        self.assertEqual(is_alive, False)
        
    def test_rule_2(self):
        map = [
            [0, 0, 1],
            [0, 1, 0],
            [1, 0 ,0]
        ]
        is_alive = check_cell(map, 1, 1)
        self.assertEqual(is_alive, True)
        map = [
            [0, 0, 1],
            [0, 1, 0],
            [1, 0 ,1]
        ]
        is_alive = check_cell(map, 1, 1)
        self.assertEqual(is_alive, True)
        
    def test_rule_3(self):
        map = [
            [1, 0, 0],
            [0, 1, 1],
            [1, 1 ,0]   
        ]
        is_alive = check_cell(map, 1, 1)
        self.assertEqual(is_alive, False)
        
    def test_rule_4(self):
        map = [
            [1, 0, 0],
            [0, 0, 1],
            [0, 1 ,0]
        ]
        is_alive = check_cell(map, 1, 1)
        self.assertEqual(is_alive, True)