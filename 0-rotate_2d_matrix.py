#!/usr/bin/python3
"""
This script defines functions to rotate a 2D matrix in-place.
"""

def transpose_matrix(matrix, n):
    """
    Transpose the given square matrix in-place.

    Args:
        matrix (list[list[_type_]]): The input square matrix.
        n (int): The size of the square matrix.
    """
    for i in range(n):
        for j in range(i, n):
            # Swap matrix elements across the main diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def reverse_matrix(matrix):
    """
    Reverse each row of the given matrix in-place.

    Args:
        matrix (list[list[_type_]]): The input matrix.
    """
    for row in matrix:
        row.reverse()

def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list[list[_type_]]): The input matrix to be rotated.
    
    Returns:
        list[list[_type_]]: The rotated matrix.
    """
    n = len(matrix)

    # Transpose matrix
    transpose_matrix(matrix, n)

    # Reverse matrix (clockwise rotation)
    reverse_matrix(matrix)

    return matrix
