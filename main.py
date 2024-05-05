#here we'll run the interface
from Problem import Problem

def main():
    val = input("Type \"1\" to enter your own puzzle, otherwise press any key to run a default puzzle: ")
    if val == "1":
        print("Enter your puzzle, use a zero to represent the blank and only spaces between numbers (don't include a space at the start or end)")
        row1 = input("Enter the first row, use space between numbers: ")
        row2 = input("Enter the second row, use space between numbers: ")
        row3 = input("Enter the third row, use space between numbers: ")

        row1 = row1.split(" ")
        row2 = row2.split(" ")
        row3 = row3.split(" ")
        
        row1 = list(map(int,row1))
        row2 = list(map(int,row2))
        row3 = list(map(int,row3))

        custom_puzzle = []
        custom_puzzle.append(row1)
        custom_puzzle.append(row2)
        custom_puzzle.append(row3)

        goalState = [[1,2,3], [4,5,6], [7,8,0]]
        print("Enter your choice of algorithm (1,2 3)")
        print("1 - Uniform Cost Search")
        print("2 - A* with the Misplaced Tile heuristic")
        print("3 - A* with the Euclidean distance heuristic")
        algo_choice = input()

        verbose = input("Would you like to see a trace of the algorithm (yes or no)? ")
        trace = (verbose == "yes")

        if algo_choice == "1":
            algo = Problem(custom_puzzle, goalState)
            algo.search()
        elif algo_choice == "2":
            algo = Problem(custom_puzzle, goalState, "Misplaced", trace)
            algo.search()
        elif algo_choice == "3":
            algo = Problem(custom_puzzle, goalState, "Euclidean", trace)
            algo.search()
    else:
        goalState = [[1,2,3], [4,5,6], [7,8,0]]
        initalState = [[8,7,1], [6, 0, 2], [5,4,3]]
        print(initalState)
        print("Running A* with Euclidean on pre-defined initial state")
        algo = Problem(initalState, goalState, "Euclidean", False)
        algo.search()



if __name__ == "__main__":
    main()