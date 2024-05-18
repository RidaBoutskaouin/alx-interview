#!/usr/bin/env python3
""" Solution to N-Queens problem"""
import sys


def backtracking(n, row, col, diag1, diag2, solutions):
    """Backtracking function to solve N-Queens problem"""
    if row == n:
        solutions.append([[r, c] for r, c in enumerate(col)])
        return
    for c in range(n):
        if c in col or row - c in diag1 or row + c in diag2:
            continue
        col.append(c)
        diag1.append(row - c)
        diag2.append(row + c)
        backtracking(n, row + 1, col, diag1, diag2, solutions)
        col.pop()
        diag1.pop()
        diag2.pop()


def nqueens(n):
    """Solves N-Queens problem"""
    if not isinstance(n, int):
        raise TypeError("n must be a number")
    if n < 4:
        raise ValueError("n must be at least 4")
    solutions = []
    backtracking(n, 0, [], [], [], solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = nqueens(n)
    for solution in solutions:
        print(solution)
