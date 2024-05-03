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
    
    def Euclidean(self):
        dist = 0
        for i in range(len(self.state)):
            for j in range(len(self.state[0])):
                print(self.state[i][j]-1)
                expected = [(self.state[i][j]-1)//3,(self.state[i][j]-1)%3]
                print(expected)
                if(expected[0] == -1):
                    expected = [2,2]
                actual = [i,j]
                print(actual)
                squared_diff = [(actual[0]-expected[0]) ** 2, (actual[1]-expected[1]) ** 2]
                print("Diff for " + str(self.state[i][j]) + " " + str(sum(squared_diff)))
                dist += sum(squared_diff)**0.5
        return dist
