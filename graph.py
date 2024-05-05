from Problem import Problem
import matplotlib.pyplot as plt

trivial = [[1,2,3], [4,5,6], [7,8,0]]
veasy = [[1,2,3], [4,5,6], [7,0,8]]
easy = [[1,2,0], [4,5,3], [7,8,6]]
trace = [[1,2,3], [4,8,0], [7,6,5]]
ohboy = [[8,7,1], [6, 0, 2], [5,4,3]]
imp = [[1,2,3], [4,5,6], [8,7,0]]
goalState = [[1,2,3], [4,5,6], [7,8,0]]

names = ["Trivial","Very easy", "Easy", "Trace", "Oh boy"]

l = [trivial, veasy, easy, trace]

maxNodesUCS = []
exploredSetUCS = []

maxNodesEuc = []
exploredSetEuc = []

maxNodesMisplaced = []
exploredSetMisplaced = []

j = 0
print("Starting")
for i in l:
    print("Doing UCS", names[j])
    print(i)
    alg = Problem(i, goalState, None, False)
    vals = alg.search()
    print("Done")
    maxNodesUCS.append(vals[1])
    exploredSetUCS.append(vals[2])
    j += 1

j = 0
for i in l:
    print("Doing EUC", names[j])
    alg = Problem(i, goalState, "Euclidean", False)
    vals = alg.search()
    maxNodesEuc.append(vals[1])
    exploredSetEuc.append(vals[2])
    j += 1

j = 0
for i in l:
    print("Doing Misplaced", names[j])
    alg = Problem(i, goalState, "Misplaced", False)
    vals = alg.search()
    maxNodesMisplaced.append(vals[1])
    exploredSetMisplaced.append(vals[2])
    j += 1


print("Uniform Cost")
print(maxNodesUCS)
print(exploredSetUCS)
print()
print()
print("A* Manhattan Heuristic")
print(maxNodesMisplaced)
print(exploredSetMisplaced)
print()
print()
print("A* Euclidean Heuristic")
print(maxNodesEuc)
print(exploredSetEuc)
print()
print()

# Plotting maxNodes
plt.figsize((10, 15))
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
plt.xticks(rotation=45)
plt.legend(title = 'Algorithm Comparison')

# Save the plot
plt.savefig('maxNodes_plot.png')
plt.close()