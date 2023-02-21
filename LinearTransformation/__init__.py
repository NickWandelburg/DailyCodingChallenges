# Compute the linear transformation of a vector
import numpy as np

def linear_transformation(vector, matrix):
    transformed_vector = np.zeros(len(vector), dtype=int)
    # Iterate over the rows of the vector and the matrix
    for i in range(len(vector)):
        # Iterate over the columns of the matrix
        for j in range(len(matrix[i])):
            # Add the product of the vector row and the matrix row/column to the transformed vector
            transformed_vector[i] += matrix[i][j] * vector[j]
    return transformed_vector


if __name__ == '__main__':
    # Define the vector and the matrix
    vector = np.array([1, 2, 3])
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    print("Vector:")
    for row in vector:
        print(row)
    print("Matrix:")
    for row in matrix:
        print(row)

    # Compute the linear transformation
    transformed_vector = linear_transformation(vector, matrix)

    print("Transformed Vector:")
    for row in transformed_vector:
        print(row)
