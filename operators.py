from Node import Node
import copy

def find(puzzle_state, target):
    for i, sublist in enumerate(puzzle_state):
        try:
            j = sublist.index(target)
        except ValueError:
            continue
        return i, j
            
    return None, None

def up(puzzle_state, i, j):
    new_state = copy.deepcopy(puzzle_state)
    if i > 0:
        temp = new_state[i - 1][j]
        new_state[i-1][j] = new_state[i][j]
        new_state[i][j] = temp
        return new_state
    else:
        return None

def down(puzzle_state, i, j):
    new_state = copy.deepcopy(puzzle_state)
    if i + 1 < len(puzzle_state):
        temp = new_state[i + 1][j]
        new_state[i + 1][j] = new_state[i][j]
        new_state[i][j] = temp
        return new_state
    else:
        return None

def left(puzzle_state, i, j):
    new_state = copy.deepcopy(puzzle_state)
    if j > 0 :
        temp = new_state[i][j - 1]
        new_state[i][j - 1] = new_state[i][j]
        new_state[i][j] = temp
        return new_state
    else:
        return None

def right(puzzle_state, i, j):
    new_state = copy.deepcopy(puzzle_state)
    if j + 1 < len(puzzle_state[0]) :
        temp = new_state[i][j + 1]
        new_state[i][j + 1] = new_state[i][j]
        new_state[i][j] = temp
        return new_state
    else:
        return None


def neighborsNode(node):
    possNodes = []
    i, j = find(node.state, 0)
    possNodes.append(Node(up(node.state, i, j), node, "up", node.depth + 1, node.heuristic))
    possNodes.append(Node(down(node.state, i, j), node, "down", node.depth + 1, node.heuristic))
    possNodes.append(Node(left(node.state, i, j), node, "left", node.depth + 1, node.heuristic))
    possNodes.append(Node(right(node.state, i, j), node, "right", node.depth + 1, node.heuristic))
    
    #check for invalid moves
    new_nodes = [currnode for currnode in possNodes if currnode.state != None]

    #don't want to explore parent again
    new_nodes = [currnode for currnode in new_nodes if node.state != currnode.state]

    return new_nodes