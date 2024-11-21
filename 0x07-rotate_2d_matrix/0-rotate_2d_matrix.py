#!/usr/bin/python3
"""
Rotate a 2D matrix 90 degrees clockwise in-place.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates the given matrix 90 degrees clockwise in-place.
    
    Args:
        matrix (list of list of int): The 2D matrix to rotate.
        
    Returns:
        None: The matrix is modified in-place.
    """
    
    # Step 1: Transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            # Swap elements at matrix[i][j] with matrix[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

