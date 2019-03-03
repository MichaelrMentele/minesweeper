import unittest
from mock import MagicMock

import Board


class TestGameManager(unittest.TestCase):
    def test_selected_mine(self):
        mock = MagicMock()
        gm = GameManager(config={saturation: 1.0})
        gm.board.is_mine = MagicMock(auto_doc=True)

        gm.selected_mine((0,0))

        self.assertTrue(gm.board.is_mine.called)


    def test_has_won(self):
        # asks the board whether
        # any of the cells that are NOT
        # mines are NOT visible
        raise

    def test_present(self):
        # should pass the board to
        # a presenter object and return
        # it presents (wraps presenter)
        raise
