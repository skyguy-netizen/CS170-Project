from Node import Node


class Problem:
    def __init__(self, initalState, goalState = None, heuristic = 0):
        self.initalState = initalState
        self.goalState = goalState

    def create_node(self, state, parent, operator, depth, cost):
        return Node(state, parent, operator, depth, cost)

    def solve():
        if heuristic == None:
            UniformCostSearch()
        else if heuristic == "Misplace Tile":
            AstarMisplacedTile()
        else:
            AstarEuclideanDistance()
    