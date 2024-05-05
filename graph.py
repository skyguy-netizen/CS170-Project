from Problem import Problem
import matplotlib.pyplot as plt

trivial = [[1,2,3], [4,5,6], [7,8,0]]
veasy = [[1,2,3], [4,5,6], [7,0,8]]
easy = [[1,2,0], [4,5,3], [7,8,6]]
trace = [[1,0,3], [4,2,6], [7,5,8]]
doable = [[0, 1,2], [4,5,3], [7,8,6]]
ohboy = [[8,7,1], [6, 0, 2], [5,4,3]]
imp = [[1,2,3], [4,5,6], [8,7,0]]
goalState = [[1,2,3], [4,5,6], [7,8,0]]

names = ["Trivial","Very easy", "Easy", "Trace", "Doable", "Our Test Case", "Oh Boy", "Impossible"]

# l = [trivial, veasy, easy, trace, doable, ohboy]

maxNodesUCS = [1, 3, 8, 14, 16, 28, 25159, 24399]
exploredSetUCS = [1, 4, 13, 27, 32, 61, 113494, 181440]

maxNodesMisplaced = [1, 3, 3, 6, 4, 9, 3884, 22611]
exploredSetMisplaced = [1, 4, 5, 9, 8, 15, 10595, 181440]

maxNodesEuc = [1, 3, 3, 6, 4, 7, 787, 20577]
exploredSetEuc = [1, 4, 5, 9, 8, 12, 2076, 181440]

# j = 0
# print("Starting")
# for i in l:
#     print("Doing UCS", names[j])
#     print(i)
#     alg = Problem(i, goalState, None, False)
#     vals = alg.search()
#     print("Done")
#     maxNodesUCS.append(vals[1])
#     exploredSetUCS.append(vals[2])
#     j += 1

# j = 0
# for i in l:
#     print("Doing EUC", names[j])
#     alg = Problem(i, goalState, "Euclidean", False)
#     vals = alg.search()
#     maxNodesEuc.append(vals[1])
#     exploredSetEuc.append(vals[2])
#     j += 1

# j = 0
# for i in l:
#     print("Doing Misplaced", names[j])
#     alg = Problem(i, goalState, "Misplaced", False)
#     vals = alg.search()
#     maxNodesMisplaced.append(vals[1])
#     exploredSetMisplaced.append(vals[2])
#     j += 1


# print("Uniform Cost")
# print(maxNodesUCS)
# print(exploredSetUCS)
# print()
# print()
# print("A* Manhattan Heuristic")
# print(maxNodesMisplaced)
# print(exploredSetMisplaced)
# print()
# print()
# print("A* Euclidean Heuristic")
# print(maxNodesEuc)
# print(exploredSetEuc)
# print()
# print()

# Plotting maxNodes
plt.figure(figsize = (15, 10))
# for i in range(len(names)):
#     plt.plot(names[i], maxNodesUCS[i], label=f"{names[i]} (UCS)", marker='o')
plt.plot(names, maxNodesUCS, label = "Uniform Cost Search", marker = 'o')

# Plotting A* results with Euclidean heuristic
# for i in range(len(names)):
    # plt.plot(names[i], maxNodesEuc[i], label=f"{names[i]} (A*, Euclidean)", marker='x')
plt.plot(names, maxNodesEuc, label = "A* with Euclidean Distance Heuristic", marker = 'x')
# plt.figure(figsize=(10, 6))
# plt.plot(names, maxNodesUCS)
# plt.plot(names, maxNodesEuc)

plt.plot(names, maxNodesMisplaced, label = "A* with Misplaced Tile Heuristic", marker = '^')

plt.xlabel('Puzzle Type')
plt.ylabel('Max Nodes')
plt.title('Max Nodes Comparison')
# plt.xticks(rotation=45)
plt.legend(title = 'Algorithm Comparison for Max Nodes in Queue')

# Save the plot
plt.savefig('maxNodes_plot.png')
plt.close()

plt.figure(figsize = (15, 10))
plt.plot(names, exploredSetUCS, label = "Uniform Cost Search", marker = 'o')
plt.plot(names, exploredSetEuc, label = "A* with Euclidean Distance Heuristic", marker = 'x')
plt.plot(names, exploredSetMisplaced, label = "A* with Misplaced Tile Heuristic", marker = '^')
plt.xlabel('Puzzle Type')
plt.ylabel('Total Expanded Nodes')
plt.title('Total Expanded Nodes Comparison')
# plt.xticks(rotation=45)
plt.legend(title = 'Algorithm Comparison for total Expanded Nodes')

# Save the plot
plt.savefig('expandedNodes_plot.png')
plt.close()