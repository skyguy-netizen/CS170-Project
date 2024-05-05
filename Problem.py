from Node import Node
import heapq as pq
from collections import defaultdict
from operators import neighborsNode, find
import math

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

    def flatten(self, state):
        l = []
        for a in state:
            l += a
        return tuple(l)
    
    def euclidean(self, node):
        dist = 0
        side_len = len(node.state) #if its a 8 puzzle, 15 puzzle, 24 puzzle, etc.
        for i in range(len(node.state)):
            for j in range(len(node.state[0])):
                if(node.state[i][j]!=0):
                    expected = [(node.state[i][j]-1)//side_len,(node.state[i][j]-1)%side_len]
                    if(expected[0] == -1):
                        expected = [side_len - 1, side_len - 1]
                    actual = [i,j]
                    squared_diff = [(actual[0]-expected[0]) ** 2, (actual[1]-expected[1]) ** 2]
                    dist += sum(squared_diff)**0.5
        return dist
    
    
    def misplaced(self, node):
        count = 0
        for i in range(len(node.state)):
            for j in range(len(node.state)):
                if(node.state[i][j]!=0):
                    if(node.state[i][j] != self.goalState[i][j]):
                        count+=1
        return count

    def search(self):
        root = Node(self.initalState)
        goal = Node(self.goalState)
        frontier = [] #priorityqueue
        pq.heappush(frontier, root)
        exploredSet = defaultdict(bool)

        maxNodes = 1

        while True:
            if not frontier:
                print("No solution")
                print("Max Queue size: ", maxNodes)
                print("Explored Nodes: ", len(exploredSet))
                return (False, maxNodes, len(exploredSet))
            maxNodes = max(maxNodes, len(frontier))
            currnode = pq.heappop(frontier)

            if self.trace == True:
                print("\nThe best state to expand with g(n) = "
                    + str(int(currnode.depth))
                    + " and h(n) = " 
                    + str(math.ceil(currnode.heuristic))
                    + " is...")
                currnode.printState()

            
            exploredSet[self.flatten(currnode.state)] = True
            if currnode == goal:
                print("Solution found")
                print("Printing solution")
                self.printSolution(currnode)
                print("Max queue size:", maxNodes)
                print("Nodes expanded:", len(exploredSet))
                return (True, maxNodes, len(exploredSet))
            else:
                candidateNodes = neighborsNode(currnode)
                for node in candidateNodes:
                    if node not in frontier and exploredSet[self.flatten(node.state)] == False:
                        node.heuristic = self.calcHeuristic(node)
                        pq.heappush(frontier, node)
        return (False, maxNodes, len(exploredSet))

    
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