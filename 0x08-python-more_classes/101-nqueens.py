#!/usr/bin/python3

"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Usage:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

The program prints every possible solution to the problem.
One solution per line.

Example:
    $ ./101-nqueens.py 4
    [[0, 1], [1, 3], [2, 0], [3, 2]]
    [[0, 2], [1, 0], [2, 3], [3, 1]]
"""

import sys

def init_chessboard(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    return [[' '] * n for _ in range(n)]

def is_safe(chessboard, row, col, n):
    """Check if it's safe to place a queen at the given position."""
    # Check the column
    for i in range(row):
        if chessboard[i][col] == 'Q':
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if chessboard[i][j] == 'Q':
            return False

    # Check upper diagonal on the right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if chessboard[i][j] == 'Q':
            return False

    return True

def solve_nqueens(chessboard, row, n):
    """Recursively solve the N-Queens puzzle and print solutions."""
    if row == n:
        print(get_solution(chessboard))
        return

    for col in range(n):
        if is_safe(chessboard, row, col, n):
            chessboard[row][col] = 'Q'
            solve_nqueens(chessboard, row + 1, n)
            chessboard[row][col] = ' '

def get_solution(chessboard):
    """Return the list of lists representation of a solved chessboard."""
    return [[r, c] for r in range(len(chessboard)) for c in range(len(chessboard)) if chessboard[r][c] == 'Q']

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    chessboard = init_chessboard(n)
    solve_nqueens(chessboard, 0, n)
