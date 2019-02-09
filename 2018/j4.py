#Store Input
length = int(input())
matrix = []
for i in range(length):
    matrix.append(input().split(" "))

def CheckForOrder(alist):
    num = alist[0]
    for i in alist:
        if i >= num:
            num = i
        else:
            return False
    return True

def CheckForOrderedRows(alist):
    for i in range(length):
        if CheckForOrder(alist[i]) == True:
            continue
        else:
            return False
    return True

def RotateMatrix(mat):
    #for x in range(0,length):
        #for y in range(x,Length-x-1):
    N = length
    for x in range(0, int(length/2)): 
        for y in range(x, N-x-1): 
            temp = mat[x][y] 
  
            mat[x][y] = mat[y][N-1-x] 
            mat[y][N-1-x] = mat[N-1-x][N-1-y] 
            mat[N-1-x][N-1-y] = mat[N-1-y][x] 
            mat[N-1-y][x] = temp 

matrixrotated = matrix
for i in range(3):
    RotateMatrix(matrixrotated)

#Driver
for i in range(4):
    if CheckForOrderedRows(matrix) == True:
        if CheckForOrderedRows(matrixrotated) == True:
            break
        else:
            RotateMatrix(matrix)
            RotateMatrix(matrixrotated)
    else:
        RotateMatrix(matrix)
        RotateMatrix(matrixrotated)

#Print Output
for i in range(length):
    print(" ".join(str(y) for y in matrix[i]))