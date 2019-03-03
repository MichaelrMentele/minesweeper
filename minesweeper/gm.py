import six

from pyfiglet import figlet_format

try:
    from termcolor import colored
except ImportError:
    colored = None

from minesweeper.board import Board
from minesweeper.presenter import Presenter


# TODO: refactor into a 'screen' object..?
def log(string, color, font="slant", figlet=False):
    if colored:
        if not figlet:
            six.print_(colored(string, color))
        else:
            six.print_(colored(figlet_format(
                string, font=font), color))
    else:
        six.print_(string)


class GameManager:
    ''' Top level manager of the game '''

    def __init__(self, board=None, presenter=None):
        self.board = board or Board()
        self.presenter = presenter or Presenter(self.board)

    def start_game(self):
        log("Minesweeper", color="blue", figlet=True)
        log("Welcome to Minesweeper!", "green")
        self.present()

    def continue_game(self):
        log("Good choice! You're still alive.", "green")
        self.present()

    def lose_game(self):
        log("You got blown to bits! Goodbye.", color="red")
        self.present_unmasked()

    def win_game(self):
        log("Huzzah! You have revealed all non-mines on the board!", color="gold")
        self.present_unmasked()

    def reveal(self, coor):
        # TODO: print some output, maybe highlight revealed square or something
        self.board.reveal(coor)

    def selected_mine(self, coor):
        return self.board.is_mine(coor)

    def has_won(self, coor):
        '''
        '''
        import ipdb; ipdb.set_trace()
        # count of NOT visible cells is equal
        # to the number of mines
        # and no mines are visible
        return False

    def present_unmasked(self):
        self.presenter.build()
        rows = self.presenter.unmasked_presentation
        [log(row, 'green') for row in rows]

    def present(self):
        self.presenter.build()
        rows = self.presenter.presentation
        [log(row, 'green') for row in rows]
