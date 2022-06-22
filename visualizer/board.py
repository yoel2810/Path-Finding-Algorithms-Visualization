import pygame
from .constants import *


class Board:
    def __init__(self) -> None:
        self.board = []
        self.start = (-1, -1)
        self.goals = set()
        self.blocks = set()

    def draw_grid(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(ROWS):
                color = WHITE
                if (row, col) == self.start:
                    color = (0, 255, 0)
                elif (row, col) in self.goals:
                    color = (255, 0, 0)
                elif (row, col) in self.blocks:
                    color = (123, 123, 123)
                self.draw_square(win, color, row, col)

    def draw_square(self, win, color, row, col):
        pygame.draw.rect(win, color, (row * SQUARE_SIZE + GAP * row,
                                      col * SQUARE_SIZE + GAP * col, SQUARE_SIZE, SQUARE_SIZE))

    def add_remove_comp(self, row, col):
        # if self.start == (row, col):
        #     self.start = (-1, -1)
        # elif (row, col) in self.goals:
        #     self.goals.remove((row, col))
        if False:
            print("need to change later")
        else:
            if not (row, col) in self.blocks:
                if self.start == (-1, -1):
                    self.start = (row, col)
                else:
                    self.goals.add((row, col))

    def add_remove_block(self, row, col):
        if (row, col) != self.start and not (row, col) in self.goals:
            if (row, col) in self.blocks:
                x = 2#self.blocks.remove((row, col))
            else:
                self.blocks.add((row, col))

    
