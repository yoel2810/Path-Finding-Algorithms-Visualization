import pygame
import time
from .constants import *


class Board:
    def __init__(self) -> None:
        self.board = []
        self.start = (-1, -1)
        self.goals = set()
        self.blocks = set()
        self.path = list()

    def draw_grid(self, win, open_list = [], closed_list = []):
        win.fill(BLACK)
        # print(self.closed_list)
        for row in range(ROWS):
            for col in range(ROWS):
                self.draw_square(win, WHITE, row, col)

        for p in self.path:
            self.draw_square(win, (0,0,255), p[0], p[1])
        for b in self.blocks:
            self.draw_square(win, (123,123,123), b[0], b[1])
        for opl in open_list:
            self.draw_square(win, (255,176,122), opl[0], opl[1])
        for cll in closed_list:
            self.draw_square(win, (255, 147, 213), cll[0], cll[1])
        self.draw_square(win, (0,255,0), self.start[0], self.start[1])
        for g in self.goals:
            self.draw_square(win, (255,0,0), g[0], g[1])

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
                x = 2  # self.blocks.remove((row, col))
            else:
                self.blocks.add((row, col))

    def add_path(self, path):
        self.path = path

    def add_open_list(self, l):
        self.open_list = l
        # print(self.open_list)
        
    
    def add_closed_list(self, l):
        self.closed_list = l
        # print(self.closed_list)
