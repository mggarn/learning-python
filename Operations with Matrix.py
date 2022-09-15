#Returns the trace of given square matrix
def matrix_trace(matrix):
    trace = 0
    size = len(matrix[0])
    for i in range(size):
        trace += int(matrix[i][i])
    return trace
    
#Prints the number of elements in each row of matrix that are greater than the arithmetic mean of the given row
def matrix_above_average(matrix):
    counter = 0
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > sum(matrix[i])/len(matrix[i]):
                counter += 1
        print(counter)
        counter = 0
       
#Returns the indices (row and column) of the first occurrence of the maximum element in matrix of any size
def matrix_max_indices(matrix):
    n = len(matrix)
    m = len(matrix[0])
    maximum = matrix[0][0]
    x, y = 0, 0

    for i in range(n):
        if max(matrix[i]) > maximum:
            maximum = max(matrix[i])
            x = i
            y = matrix[i].index(maximum)

    return (x, y)
    
#Swaps columns in a matrix
def matrix_swap_cols(matrix, x, y):
    for l in range(n):
        matrix[l][x], matrix[l][y] = matrix[l][y], matrix[l][x]
        print(*matrix[l])
        
#Checks if a square matrix is symmetrical about the main diagonal
def matrix_is_symm(matrix):
    is_symm = True
    n = len(matrix[0])
    
    for i in range(n):
        for j in range(n):
            if i > j and matrix[i][j] != matrix[j][i]:
                is_symm = False
                break
        if not is_symm:
            return is_symm
    else:
        return is_symm
