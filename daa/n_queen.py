# Python3 program to solve N Queen Problem and print all possible solutions

def printSolution(board, N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()  # Print a newline to separate different solutions


# A utility function to check if a queen can be placed on board[row][col]
def isSafe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQUtil(board, col, N, solutions):
    # Base case: If all queens are placed
    if col >= N:
        # Store the solution as a deep copy of the board
        solutions.append([row[:] for row in board])
        return

    # Try placing queen in each row of this column
    for i in range(N):
        if isSafe(board, i, col, N):
            board[i][col] = 1  # Place the queen

            # Recur to place the rest of the queens
            solveNQUtil(board, col + 1, N, solutions)

            board[i][col] = 0  # Backtrack


def solveNQ(N):
    # Initialize the board with 0s
    board = [[0] * N for _ in range(N)]
    solutions = []  # List to store all solutions

    solveNQUtil(board, 0, N, solutions)

    if not solutions:
        print("Solution does not exist")
    else:
        print(f"Total solutions: {len(solutions)}\n")
        for sol in solutions:
            printSolution(sol, N)


# Driver Code
if __name__ == '__main__':
    try:
        N = int(input("Enter the number of queens (N): "))
        if N < 1:
            print("Please enter a positive integer.")
        else:
            solveNQ(N)
    except ValueError:
        print("Invalid input. Please enter an integer.")
