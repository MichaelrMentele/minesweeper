class Presenter:
    '''
    Takes a board and turns it into an ascii based grid.

    Ex.
    [
        [A, B]
        [C, D]
    ]

    Where:
    - A is a mine
    - B is revealed
    - C and D are not revealed

    +===+===+
    |   | 1 |
    +===+===+
    |   |   |
    +===+===+

    If the unmasked option is passed then the board becomes:

    +===+===+
    | @ | 1 |
    +===+===+
    | 1 | 1 |
    +===+===+
    '''

    def __init__(self, board):
        self.board = board.board

    def build(self):
        self.presentation = self.build_presentation()
        self.unmasked_presentation = self.build_presentation(masked=False)

    def build_presentation(self, masked=True):
        rows = []
        for row in self.board:
            rows.append(self.build_row_head(row))
            rows.append(self.build_row(row, masked=masked))
        rows.append(self.build_row_head(row))
        return rows

    @classmethod
    def build_row(self, row, masked=True):
        '''
        When masked we will not display cells that are not
        set to visible.

        Otherwise, display all.
        '''
        so_far = ''
        for cell in row:
            if cell.is_mine:
                symbol = '@'
            else:
                symbol = str(cell.adj_mine_count)

            if masked and not cell.is_visible:
                symbol = ' '

            so_far += '| ' + symbol + ' '
        return so_far + '|'

    @classmethod
    def build_row_head(self, row):
        so_far = ''
        for _ in row:
            so_far += '+==='
        return so_far + '+'
