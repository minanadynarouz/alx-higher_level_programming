#!/usr/bin/python3
"""Solving N-queens problem"""

from sys import argv


def user_input():
    """Validating user input"""
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)
    return n


def is_safe(board, row, col, n):
    """Check if there is a queen in the same row to the left"""
    for i in range(col):
        if board[i] == row or \
                board[i] - i == row - col or \
                board[i] + i == row + col:
            return False
    return True


def printSolution(board):
    """Print the solutions"""
    solutions = []
    for i in range(len(board)):
        solutions.append([i, board[i]])
    print(solutions)


def solveQueenUntil(board, col, n):
    """Backtracking to solve the queen"""
    if col == n:
        printSolution(board)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[col] = i
            solveQueenUntil(board, col + 1, n)


def solveQueens():
    """Implementation of the solutions"""
    n = user_input()
    board = [-1] * n
    solveQueenUntil(board, 0, n)


if __name__ == "__main__":
    solveQueens()
