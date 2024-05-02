class Node:
    def __init__(self, state, parent = None, operator = None):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.path_cost = None
        self.heuristic = None
        self.depth = None

    def __eq__(self, otherState):
        return self.state == otherState.state
    
    def __hash__(self):
        return hash(self.state)

    def printState(self):
        print(self.state)
        return