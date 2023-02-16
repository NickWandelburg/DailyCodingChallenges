# Compute the transpose of a square matrix
def transpose(matrix):
    transposed_matrix = []
    # Iterate over the columns
    for i in range(len(matrix[0])):
        row = []
        # Iterate over the rows
        for j in range(len(matrix)):
            # Append the element at the current row and column to the row
            row.append(matrix[j][i])
        # Append the row to the transposed matrix
        transposed_matrix.append(row)
    return transposed_matrix


if __name__ == '__main__':
    # Generate a 3x3 matrix
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Transpose the matrix
    transposed_matrix = transpose(matrix)

    # Alternatively, with list comprehension
    # transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    print('Original matrix:')
    for row in matrix:
        print(row)
    print('Transposed matrix:')
    for row in transposed_matrix:
        print(row)


