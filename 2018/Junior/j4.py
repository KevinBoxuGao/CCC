#Store Input
length = int(input())
matrix = []
for i in range(length):
    matrix.append([int(i) for i in input().split(" ")])

def CheckForOrder(aList):
    num = aList[0]
    for i in aList:
        if i >= num:
            num = i
        else:
            return False
    return True

def CheckForRows(aList):
    for i in aList:
        if CheckForOrder(i) == True:
            continue
        else:
            return False
    return True

def CheckForColumns(aList):
    for i in range(length):
        Column = [row[i] for row in aList]
        if CheckForOrder(Column) == True:
            continue
        else:
            return False
    return True





def reverseColumns(arr): 
    for i in range(length): 
        j = 0
        k = length-1
        while j < k: 
            t = arr[j][i] 
            arr[j][i] = arr[k][i] 
            arr[k][i] = t 
            j += 1
            k -= 1
    
# Function for do transpose of matrix 
def transpose(arr): 
    for i in range(length): 
        for j in range(i, length): 
            temp = arr[i][j] 
            arr[i][j] = arr[j][i] 
            arr[j][i] = temp 
   
def rotateMatrix(arr): 
    transpose(arr) 
    reverseColumns(arr)





#Driver
for i in range(4):
    if CheckForRows(matrix) == True:
        if CheckForColumns(matrix) == True:
            break
        else:
            rotateMatrix(matrix)
    else:
        rotateMatrix(matrix)

#Print Output
for i in range(length):
    print(" ".join(str(y) for y in matrix[i]))