import unittest
from mock import MagicMock

import Board


class TestBoard(unittest.TestCase):
    def test_is_mine(self):
        self.assertTrue(Board(saturation=1.0).is_mine((0,0)))
        self.assertFalse(Board(saturation=0.0).is_mine((0,0)))

    def test_reveal_cell(self):
        # annotate the cell as visible
        raise

    def test_adj_mines(self):
        # return a count of all mines adj, diagonal
        # inclusive

    def test_init(self):
        # initializes with num of mines == saturation()
        # default is 25%
        
