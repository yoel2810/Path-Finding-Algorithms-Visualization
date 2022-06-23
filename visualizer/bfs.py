import pygame

from visualizer.node import Node
from .constants import *
from queue import Queue

class BFS:
    def __init__(self, board, win) -> None:
        self.board = board
        self.win = win

    def run(self):

        if self.board.start in self.board.goals:
            return "\nNum: 0\nCost: 0\nTime: "
        
        nodeNumber = 0
        start = self.board.start
        L = Queue()
        openList = {}
        current = Node(list(), start[0], start[1])
        L.put(current)
        openList[start] = current
        nodeNumber += 1
        closedList = {}

        while L.qsize() > 0:
            n = L.get()
            self.board.draw_grid(self.win, openList, closedList)
            pygame.display.update()
            openList.pop(n.get_current())
            closedList[n.current] = n

            operators = n.get_operators(self.board)
            for operatorKey in operators:
                op = operators[operatorKey]
                nodeNumber += 1
                if not operatorKey in openList and not operatorKey in closedList:
                    if operatorKey in self.board.goals:
                        self.board.add_path(op.path)
                        # self.board.add_open_list([])
                        # self.board.add_closed_list([])
                        return
                    L.put(op)
                    openList[operatorKey] = op
        print("no path\n")
        return "no path\n"