from .constants import *


class Node:
    def __init__(self, path, row, col) -> None:
        self.current = (row, col)
        self.path = path.copy()
        self.path.append((row, col))
        self.row = row
        self.col = col

    def move_up(self, grid):
        i, j = self.current
        if i <= 0 or (i - 1, j) in grid.blocks:
            return None
        return Node(self.path, i - 1, j)

    def move_down(self, grid):
        i, j = self.current
        if i >= SIZE - 1 or (i + 1, j) in grid.blocks:
            return None
        return Node(self.path, i + 1, j)

    def move_right(self, grid):
        i, j = self.current
        if j >= SIZE - 1 or (i, j + 1) in grid.blocks:
            return None
        return Node(self.path, i, j + 1)

    def move_left(self, grid):
        i, j = self.current
        if j <= 0 or (i, j - 1) in grid.blocks:
            return None
        return Node(self.path, i, j - 1)

    def get_operators(self, grid):
        operationList = {}
        operators = [None] * 4
        operators[0] = self.move_up(grid)
        operators[1] = self.move_left(grid)
        operators[2] = self.move_down(grid)
        operators[3] = self.move_right(grid)

        for o in operators:
            if not o is None:
                operationList[(o.row, o.col)] = o
        return operationList

    def get_current(self):
        return self.current
