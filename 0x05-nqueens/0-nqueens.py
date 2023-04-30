#!/usr/bin/python3
import sys


def is_valid(board, row, col):
    for r, c in board:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def n_queens_helper(n, row, board, solutions):
    if row == n:
        solutions.append(board[:])
    else:
        for col in range(n):
            if is_valid(board, row, col):
                board.append((row, col))
                n_queens_helper(n, row + 1, board, solutions)
                board.pop()


def n_queens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    elif n < 4:
        print("N must be at least 4")
        sys.exit(1)
    else:
        solutions = []
        n_queens_helper(n, 0, [], solutions)
        for solution in solutions:
            print(solution)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    n_queens(n)
