import math
import sys

N = int(input())
M = int(input())

grid = [M*[None]]
marked = [(M+1)*[False] for i in range(N+1)]

result = "no"

for i in range(N):
    row = [int(i) for i in sys.stdin.readline().split()]
    row.insert(0, None)
    grid.append(row)

marked[1][1] = True


def factors(number):
    result = []
    factors = []
    if number == 1:
        factors.append([number, 1])
    else:
        factors.append([number, 1])
        factors.append([1, number])

    for i in range(2, (number//2)+1):
        if number % i == 0:
            factors.append([i, number//i])

    for i in factors:
        if i[0] <= N and i[1] <= M:
            result.append(i)
    return result


def DFS(row, column):
    global result
    if result == "yes":
        return

    if row == N and column == M:
        result = "yes"
        return

    possibleJumps = factors(grid[row][column])

    for jump in possibleJumps:
        curRow = jump[0] 
        curColumn = jump[1] 

        if marked[curRow][curColumn] == True:
            return
        else: 
            marked[curRow][curColumn] = True
            DFS(curRow, curColumn)


DFS(1,1)

print(result)
