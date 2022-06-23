import sys
import pygame

from visualizer.node import Node
from .constants import *
from queue import Queue
from collections import deque

class Algorithm:
    def __init__(self, board, win) -> None:
        self.board = board
        self.win = win

    def dfs(self):
        H = {}
        start = self.board.start
        result = self.limitedDFS(Node(list(), start[0], start[1]), self.board.goals, sys.maxsize, H)
        # L = deque()
        # start = self.board.start
        # L.append(Node(list(), start[0], start[1]))
        # while len(L) > 0:
        #     self.board.draw_grid(self.win, [], [x.current for x in L])
        #     pygame.display.update()
        #     n = L.pop()
        #     operators = n.get_operators(self.board)
        #     for operatorKey in operators:
        #         op = operators[operatorKey]
        #         if op.current in self.board.goals:
        #             self.board.add_path(op.path)
        #             return "path"
        #         L.append(op)
        # return "no path\n"

    def limitedDFS(self, n, goals, limit, H):
        self.board.draw_grid(self.win, [], H)
        pygame.display.update()
        cutoff = "cutoff"
        if n.current in goals:
            self.board.add_path(n.path)
            return "path"
        
        if limit == 0:
            return cutoff

        H[n.current] = n
        isCutoff = False
        operators = n.get_operators(self.board)
        for operatorKey in operators:
                op = operators[operatorKey]
                if operatorKey in H:
                    continue
                result = self.limitedDFS(op, goals, limit - 1, H)
                if result == cutoff:
                    isCutoff = True
                elif not result == "fail":
                    return result
        
        H.pop(n.current)
        if isCutoff:
            return cutoff
        else:
            return "fail"

    def dfid(self):
        for depth in range(0, SIZE):
            H = {}
            start = self.board.start
            result = self.limitedDFS(Node(list(), start[0], start[1]), self.board.goals, depth, H)
            if not result == "cutoff":
                return result
            if result == "fail":
                return "no path\n"
        return "no path\n"


    def bfs(self):

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