#!/usr/bin/python3
"""N Queens placement on NxN chessboard"""

import sys


def generate_solutions(row, n):
    """Generate all possible solutions
    for placing queens on the chessboard."""
    solutions = [[]]
    for queen_row in range(row):
        solutions = place_queen(queen_row, n, solutions)
    return solutions


def place_queen(queen_row, board_size, prev_solutions):
    """Place a queen on the chessboard and find
    safe positions for the next queen."""
    safe_positions = []
    for solution in prev_solutions:
        for column in range(board_size):
            if is_safe(queen_row, column, solution):
                safe_positions.append(solution + [column])
    return safe_positions


def is_safe(row, column, solution):
    """Check if placing a queen at
    the given position is safe."""
    return column not in solution and all(abs(solution[col] -\
                                              column) != row - col for col in range(row))


def init():
    """Initialize the program by parsing command
    line arguments and validating N."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    return board_size


def n_queens():
    """Main function to find and print N Queens solutions."""
    board_size = init()
    # Generate all solutions
    solutions = generate_solutions(board_size, board_size)
    # Print solutions
    for solution in solutions:
        clean_solution = [[row, column] for row, column in enumerate(solution)]
        print(clean_solution)


if __name__ == '__main__':
    n_queens()
