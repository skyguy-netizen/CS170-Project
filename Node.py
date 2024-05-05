class Node:
    def __init__(self, state, parent = None, operator = None, depth = 0, heuristic = 0):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.heuristic = heuristic
        self.depth = depth

    def __eq__(self, otherState):
        return self.state == otherState.state

    #used to compare in heapq
    #source: https://stackoverflow.com/a/59956131
    def __lt__(self, otherState):
        return (self.heuristic + self.depth) <= (otherState.heuristic + otherState.depth)
    
    def find(self, puzzle_state, target):
        for i, sublist in enumerate(puzzle_state):
            try:
                j = sublist.index(target)
            except ValueError:
                continue
            return i, j
                
        return None, None

    def printState(self):
        self.printMove()
        for i in self.state:
            print(i)
        print()
        print()
        return

    def printMove(self):
        if self.operator:
            i, j = self.find(self.state, 0)
            if self.operator == "up":
                print("Move",self.state[i+1][j], "down")
            elif self.operator == "down":
                print("Move",self.state[i-1][j], "up")
            elif self.operator == "right":
                print("Move",self.state[i][j - 1], "left")
            elif self.operator == "left":
                print("Move", self.state[i][j + 1], "right")
            else:
                return
