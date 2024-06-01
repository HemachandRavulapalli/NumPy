import numpy as np

# Task 2

# Create two 2x2 matrices
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)

# Perform matrix multiplication
result_matrix = np.dot(matrix_a, matrix_b)
print("Result of Matrix Multiplication:\n", result_matrix)
