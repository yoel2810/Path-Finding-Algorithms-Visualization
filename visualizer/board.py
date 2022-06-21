from ctypes.wintypes import SIZE
from tkinter.tix import ROW
import pygame
from .constants import *


class Board:
    def __init__(self) -> None:
        self.board = []
        self.selected_piece = None
        self.start = (-1, -1)
        self.goals = []

    def draw_grid(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(ROWS):
                color = WHITE
                if (row, col) == self.start:
                    color = (123, 123, 123)
                elif (row, col) in self.goals:
                    color = (255, 0, 0)
                self.draw_square(win, color, row, col)

    def draw_square(self, win, color, row, col):
        pygame.draw.rect(win, color, (row * SQUARE_SIZE + GAP * row,
                                      col * SQUARE_SIZE + GAP * col, SQUARE_SIZE, SQUARE_SIZE))

    def add_comp(self, row, col):
        if self.start == (-1, -1):
            self.start = (row, col)
        else:
            self.goals.append((row, col))
