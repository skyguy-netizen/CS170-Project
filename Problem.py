from Node import Node
import heapq as pq
from collections import defaultdict
from operators import neighborsNode, find

class Problem:
    def __init__(self, initalState, goalState = None, heuristic = None, trace = False):
        self.initalState = initalState
        self.goalState = goalState
        self.heuristic = heuristic
        self.trace = trace

    def calcHeuristic(self, node: Node):
        if self.heuristic is None:
            return 0
        elif self.heuristic == "Euclidean":
            return self.euclidean(node)
        elif self.heuristic == "Misplaced":
            return self.misplaced(node)
        else:
            return 0

    def euclidean(self, node):
        dist = 0
        for i in range(len(node.state)):
            for j in range(len(node.state[0])):
                expected = [(node.state[i][j]-1)//3,(node.state[i][j]-1)%3]
                if(expected[0] == -1):
                    expected = [2,2]
                actual = [i,j]
                squared_diff = [(actual[0]-expected[0]) ** 2, (actual[1]-expected[1]) ** 2]
                dist += sum(squared_diff)**0.5
        return dist
    
    
    def misplaced(self, node):
        count = 0
        for i in range(len(node.state)):
            for j in range(len(node.state)):
                if(node.state[i][j]!=0):
                    if(node.state[i][j] != goalState[i][j]):
                        count+=1
        return count
    
    def fix(self, state):
        return tuple(map(tuple, state))

    def search(self):
        root = Node(initalState)
        goal = Node(goalState)
        frontier = [] #priorityqueue
        pq.heappush(frontier, root)
        exploredSet = set()

        maxNodes = 1

        while True:
            if not frontier:
                return False
            maxNodes = max(maxNodes, len(frontier))
            currnode = pq.heappop(frontier)

            if self.trace == True:
                print("\nThe best state to expand with g(n) = "
                    + str(int(currnode.depth))
                    + " and h(n) = " 
                    + str(int(currnode.heuristic))
                    + " is...")
                currnode.printState()

            
            exploredSet.add(self.fix(currnode.state))
            if currnode == goal:
                print("Solution found")
                print("Printing solution")
                self.printSolution(currnode)
                print("Max queue size:", maxNodes)
                print("Nodes expanded:", len(exploredSet))
                return True
            else:
                candidateNodes = neighborsNode(currnode)
                for node in candidateNodes:
                    if node not in frontier and self.fix(node.state) not in exploredSet:
                        node.heuristic = self.calcHeuristic(node)
                        pq.heappush(frontier, node)
        return False

    
    def printSolution(self, node: Node):
        sol_path = []
        currnode = node
        while (currnode):
            sol_path.append(currnode)
            currnode = currnode.parent
        
        sol_path = sol_path[::-1]
        for a in sol_path:
            a.printState()
        
        return
    
# initalState = [[1,2,3], [4,5,6], [7,8,0]] #trivial
# initalState = [[1,2,3], [4,5,6], [7,0,8]] #very easy
# initalState = [[1,2,0], [4,5,3], [7,8,6]] #easy
# initalState = [[0,1,2], [4,5,3], [7,8,6]] #doable
# initalState = [[1,2,3], [4,8,0], [7,6,5]] #trace
initalState = [[8,7,1], [6, 0, 2], [5,4,3]] #oh boy
# initalState = [[1,2,3], [4,5,6], [8,7,0]] #impossible
goalState = [[1,2,3], [4,5,6], [7,8,0]]

# alg = Problem(initalState, goalState, "Misplaced", False)
alg = Problem(initalState, goalState, "Euclidean", False)
# alg = Problem(initalState, goalState, False)
alg.search()