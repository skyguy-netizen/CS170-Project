#here we'll run the interface
from Problem import Problem

def main():
    val = input("Type \"1\" to enter your own puzzle, otherwise press any key to escape:")
    print(val)
    if val == "1":
        print("Enter your puzzle, use a zero to represent the blank")
        row1 = input("Enter the first row, use space or tabs between numbers:")
        row2 = input("Enter the second row, use space or tabs between numbers:")
        row3 = input("Enter the third row, use space or tabs between numbers:")

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

        print("Enter your choice of algorithm")
        print("1 - Uniform Cost Search")
        print("2 - A* with the Misplaced Tile heuristic")
        print("3 - A* with the Euclidean distance heuristic")
        algo_choice = input()
        print(algo_choice)

        if algo_choice == "1":
            print("in here 1")
        elif algo_choice == "2":
            print("in here 2")
        elif algo_choice == "3":
            print("in here 3")


    else:
        print("end of program")
    pass


if __name__ == "__main__":
    main()