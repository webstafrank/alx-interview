#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_nqueens(n):
    """Solve the N queens problem using backtracking."""
    def backtrack(row):
        if row == n:
            # A valid configuration is found, print it
            solution = [[i, board[i]] for i in range(n)]
            print(solution)
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Backtrack

    board = [-1] * n
    backtrack(0)

if __name__ == "__main__":
    # Check the number of command line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)

