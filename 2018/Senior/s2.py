growth = []
N = int(input())
for i in range(N):
    row = [int(i) for i in input().split()]
    growth.append(row)

#check rows
def checkRows():
    sortedRows = 0
    for i in range(N):
        smallest = 0
        correctNumbers = 0
        for j in range(N):
            if growth[i][j] > smallest:
                smallest = growth[i][j]
                correctNumbers = correctNumbers + 1
        if correctNumbers == N:
            sortedRows = sortedRows + 1
    if sortedRows == N:
        return True
    else:
        return False

#check columns
def checkColumns():
    sortedColumns = 0
    for i in range(N):
        smallest = 0
        correctNumbers = 0
        for j in range(N):
            if growth[j][i] > smallest:
                smallest = growth[j][i]
                correctNumbers = correctNumbers + 1
        if correctNumbers == N:
            sortedColumns = sortedColumns + 1
    if sortedColumns == N:
        return True
    else:
        return False

#check after rotation
for i in range(4):
    if checkColumns() == True and checkRows() == True:
        break
    else:
        growth = list(zip(*reversed(growth))) #rotate list 90 degrees   

#output
for i in range(N):
    row = [str(x) for x in growth[i]]
    print(" ".join(row))