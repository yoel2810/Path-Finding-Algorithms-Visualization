from visualizer.node import Node
from .constants import *
from queue import Queue

class BFS:
    def __init__(self, board) -> None:
        self.board = board

    def run(self):

        if self.board.start in self.board.goals:
            return "\nNum: 0\nCost: 0\nTime: "
        
        nodeNumber = 0
        start = self.board.start
        L = Queue()
        openList = {}
        current = Node([], start[0], start[1])
        L.put(current)
        openList[start] = current
        nodeNumber += 1
        closedList = {}

        while L:
            n = L.get()
            n_pos = n.get_current()
            openList.pop(n_pos)
            closedList[n.current] = n

            operators = n.get_operators(self.board)
            for op in operators:
                nodeNumber += 1
                operatorKey = op[0]
                if not operatorKey in openList and not operatorKey in closedList:
                    if operatorKey in self.board.goals:
                        # return getPath(op) + "\nNum: " + nodeNumber + "\nCost: "
								# + op.getValue().getCost() + "\nTime: ";
                        print(op.path)
                        return
                    L.put(op)
                    openList[operatorKey] = op
        return "no path\n"