length = 4
A = [[1,2,3,4],
     [5,6,7,8], 
     [1,2,3,4],
     [5,6,7,8]]

def CheckForColumns(aList):
    for i in range(length):
        print([row[i] for row in aList])

CheckForColumns(A)