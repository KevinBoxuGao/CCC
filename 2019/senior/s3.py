xCount = 0
rowXCount = [0, 0, 0]
columnXCount = [0, 0, 0]
grid = []
for i in range(3):
    row = input().split()
    result = []
    for j, item in enumerate(row):
        if item == "X":
            xCount += 1
            rowXCount[i] += 1
            columnXCount[j] += 1
            result.append(item)
        else:
            result.append(int(item))
    grid.append(result)

# fill in rows and columns with 2 items


def fillRow(row):
    global xCount
    xCoord = []
    for column in range(3):
        if grid[row][column] == "X":
            xCoord.append(column)
    if len(xCoord) == 1:
        xCount -= 1
        if xCoord[0] == 0:
            grid[row][0] = 2*grid[row][1] - grid[row][2]
        elif xCoord[0] == 1:
            grid[row][1] = grid[row][0] + ((grid[row][2] - grid[row][0])//2)
        else:
            grid[row][2] = 2*grid[row][1] - grid[row][0]
        xCount -= 1
        rowXCount[row] -= 1
        columnXCount[xCoord[0]] -= 1
        # check to see if the column can be filled in
        fillColumn(i)
    else:
        return


def fillColumn(column):
    global xCount
    xCoord = []
    for row in range(3):
        if grid[row][column] == "X":
            xCoord.append(row)
    if len(xCoord) == 1:
        xCount -= 1
        if xCoord[0] == 0:
            grid[0][column] = 2*grid[1][column] - grid[2][column]
        elif xCoord[0] == 1:
            grid[1][column] = grid[0][column] + \
                ((grid[2][column] - grid[0][column])//2)
        else:
            grid[2][column] = 2*grid[1][column] - grid[0][column]

        xCount -= 1
        rowXCount[xCoord[0]] -= 1
        columnXCount[row] -= 1
        # check to see if the row can be filled in
        fillRow(i)
    else:
        return


def fillGridRows():
    fullRow = 0


def fillGridColumns():

    # main


def main():
    # fill in rows with 2 items
    for i in range(3):
        fillRow(i)
        fillColumn(i)
    if xCount > 0:

        # output result
main()
for row in grid:
    result = [str(i) for i in row]
    print(" ".join(result))
