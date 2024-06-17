def init(source, target):
    numrows = len(source) + 1
    numcolumn = len(target) + 1

    # Create matrix
    matrix = [[0] * numcolumn for _ in range(numrows)]

    # Initialize first row and first column
    for c in range(numcolumn):
        matrix[0][c] = c
    for r in range(numrows):
        matrix[r][0] = r
    
    return matrix

def dis(source, target):
    matrix = init(source, target)
    numrows = len(source)
    numcolumn = len(target)
    
    # Fill the rest of the matrix
    for i in range(1, numrows + 1):
        for j in range(1, numcolumn + 1):
            del_cost = matrix[i-1][j] + 1
            ins_cost = matrix[i][j-1] + 1
            sub_cost = matrix[i-1][j-1] + (0 if source[i-1] == target[j-1] else 1)
            matrix[i][j] = min(del_cost, ins_cost, sub_cost)
    
    return matrix[numrows][numcolumn], matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Get input from user
source = str(input('Enter source: '))
target = str(input('Enter target: '))

# Calculate distance and get matrix
distance, matrix = dis(source, target)

# Print results
print("Khoảng cách Levenshtein giữa '{}' và '{}' là {}".format(source, target, distance))
print("Ma trận khoảng cách:")
print_matrix(matrix)

