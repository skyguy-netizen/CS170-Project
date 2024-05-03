from Node import Node
import heapq as pq
from collections import defaultdict
from operators import neighborsNode

class UniformCostSearch:
    def __init__(self, initalState, goalState):
        self.initalState = initalState
        self.goalState = goalState
    

    def flatten(self, state):
        l = []
        for a in state:
            l += a
        return tuple(l)

    def search(self):
        root = Node(initalState)
        goal = Node(goalState)
        frontier = [] #priorityqueue
        pq.heappush(frontier, root)
        exploredSet = defaultdict(bool)

        maxNodes = 1

        while True:
            if not frontier:
                return False
            maxNodes = max(maxNodes, len(frontier))
            currnode = pq.heappop(frontier)

            exploredSet[self.flatten(currnode.state)] = True
            # try:
            #     currnode.parent.printState()
            # except:
            #     None
            # currnode.printState()
            # print("-----------")
            print(maxNodes)
            if currnode == goal:
                print("Solution found")
                print("Max queue size: ", maxNodes)
                return True
            else:
                candidateNodes = neighborsNode(currnode)
                for node in candidateNodes:
                    if node not in frontier and exploredSet[self.flatten(node.state)] == False:
                        pq.heappush(frontier, node)
                    # else:
                        # print("Skipped")
                        # print(node not in frontier)
                        # print(exploredSet[self.flatten(node.state)] == False) 
        return False

# initalState = [[1,2,3], [4,5,6], [7,8,0]] #trivial
# initalState = [[1,2,3], [4,5,6], [7,0,8]] #very easy
# initalState = [[1,2,0], [4,5,3], [7,8,6]] #easy
# initalState = [[0,1,2], [4,5,3], [7,8,6]] #doable
initalState = [[8,7,1], [6, 0, 2], [5,4,3]] #oh boy
# initalState = [[1,2,3], [4,5,6], [8,7,0]] #impossible
goalState = [[1,2,3], [4,5,6], [7,8,0]]

alg = UniformCostSearch(initalState, goalState)
alg.search()