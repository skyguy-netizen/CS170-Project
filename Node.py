class Node:
    def __init__(self, state, parent = None, operator = None, depth = 0, heuristic = 0):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.path_cost = None
        self.heuristic = heuristic
        self.depth = depth

    def __eq__(self, otherState):
        return self.state == otherState.state

    #used to compare in heapq
    #source: https://stackoverflow.com/a/59956131
    def __lt__(self, otherState):
        return (self.heuristic + self.depth) < (otherState.heuristic + otherState.depth)
    
    def __hash__(self):
        return hash(self.state)

    def printState(self):
        for i in self.state:
            print(i)
        print()
        print()
        return