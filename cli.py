import click
import six

from minesweeper.gm import GameManager


@click.command()
def minesweeper():
    """
    Simple CLI for playing minesweeper

    >>> print('wooo')
    woo
    >>> 2 + 2
    4
    """

    # initialize GM
    gm = GameManager()
    gm.start_game()
    while True:
        coor = list(map(
            int,
            click.prompt('Select a cell by coordinate i.e. (0,0)', type=str
        ).split()))
        gm.reveal(coor) # a cell has been selected
        if gm.selected_mine(coor): # selecting this cell kills the player
            gm.lose_game()
            break
        elif gm.has_won(coor):
            gm.win_game()
            break
        else:
            gm.continue_game()


if __name__ == '__main__':
    minesweeper()
