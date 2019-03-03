from random import randint


class Board:
    def __init__(self, rows=9, cols=9, mine_saturation=0.20):
        self.num_rows, self.num_cols = rows, cols
        self.board = [[] for row in range(rows)]
        self.mine_saturation = mine_saturation
        for row in range(rows):
            for col in range(cols):
                self.board[row].append(Cell(row, col))
        self.add_mines()
        self.annotate_mine_adjacency_counts()

    def is_mine(self, coor) -> bool:
        row, col = coor
        return self.board[row][col].is_mine

    def add_mines(self) -> None:
        '''
        Side Effect:
            Randomly label cells as mines based on saturation.
        '''
        # TODO: determine whether we want the number of mines as
        # saturation * num_cells or if we want that as an upper bound
        # (as implemented)
        mine_upper_bound = int(self.mine_saturation * self.num_rows * self.num_cols)
        for _ in range(mine_upper_bound):
            randcol = randint(0, self.num_cols-1)
            randrow = randint(0, self.num_rows-1)
            self.board[randrow][randcol].is_mine = True

    def annotate_mine_adjacency_counts(self) -> None:
        # for each cell that is NOT a mine
        # ocmpute the number of adj cells that ARE mines
        # store them
        mines = []
        for row in self.board:
            for cell in row:
                if cell.is_mine:
                    mines.append(cell)

        def adj_coors(cell):
            adj = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    candidate = (cell.row - i, cell.col - j)
                    if self.in_bounds(candidate):
                        adj.append(candidate)
            return adj

        for mine in mines:
            mine.adj_mine_count = len(adj_coors(mine))

    def in_bounds(self, coor):
        return (
            coor[0] >= 0 and
            coor[0] <  self.num_rows and
            coor[1] >= 0 and
            coor[1] <  self.num_cols
        )

    def reveal(self, coor: tuple) -> bool:
        row, col = coor
        self.board[row][col].is_visible = True

# TODO: consider just using a named tuple
class Cell:
    def __init__(self, row, col, is_mine=False, is_visible=False):
        self.row, self.col = row, col
        self.is_mine = is_mine
        self.is_visible = False
        self.adj_mine_count = 0
