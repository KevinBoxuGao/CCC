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
        if xCoord[0] == 0:
            grid[0][column] = 2*grid[1][column] - grid[2][column]
        elif xCoord[0] == 1:
            grid[1][column] = grid[0][column] + \
                ((grid[2][column] - grid[0][column])//2)
        else:
            grid[2][column] = 2*grid[1][column] - grid[0][column]

        xCount -= 1
        rowXCount[xCoord[0]] -= 1
        columnXCount[column] -= 1
        # check to see if the row can be filled in
        fillRow(i)
    else:
        return


def fourX():
    global xCount
    fullRow = None
    fullColumn = None
    for i in range(3):
        if rowXCount[i] == 0:
            fullRow = i
        if columnXCount[i] == 0:
            fullColumn = i

    if fullRow == 0:
        difference = grid[1][fullColumn] - grid[0][fullColumn]
        for i in range(1, 3):
            for j in range(3):
                if grid[i][j] == "X":
                    grid[i][j] = grid[i-1][j] + difference

    elif fullRow == 1:
        difference = grid[2][fullColumn] - grid[1][fullColumn]
        i = 0
        for j in range(3):
            if grid[i][j] == "X":
                grid[i][j] = grid[i+1][j] - difference

        i = 2
        for j in range(3):
            if grid[i][j] == "X":
                grid[i][j] = grid[i-1][j] + difference

    elif fullRow == 2:
        difference = grid[2][fullColumn] - grid[1][fullColumn]
        for i in range(1, -1, -1):
            for j in range(3):
                if grid[i][j] == "X":
                    grid[i][j] = grid[i+1][j] - difference

    xCount -= 4


def sixX():
    global xCount
    fullRow = None
    fullColumn = None
    for i, row in enumerate(rowXCount):
        if row == 0:
            fullRow = i
    for i, column in enumerate(columnXCount):
        if column == 0:
            fullColumn = i
    if fullRow != None or fullColumn != None:
        if fullRow != None:
            for i in range(3):
                for j in range(3):
                    grid[i][j] = grid[fullRow][j]
        else:
            for i in range(3):
                for j in range(3):
                    grid[i][j] = grid[i][fullColumn]

    else:
        if grid[1][1] == "X":
            if grid[0][1] == "X":
                grid[1][1] = grid[2][1]
            else:
                grid[1][1] = grid[0][1]
            xCount -= 1
            rowXCount[1] -= 1
            columnXCount[1] -= 1
        else:
            grid[2][1] = grid[1][1]
            grid[0][1] = grid[1][1]
            xCount -= 2
            rowXCount[0] -= 1
            rowXCount[2] -= 0
            columnXCount[1] = 0

        fillRowsAndColumns()


def sevenX():
    global xCount
    if grid[1][1] == "X":
        if grid[0][1] != "X":
            grid[1][1] = grid[0][1]
        elif grid[2][1] != "X":
            grid[1][1] = grid[2][1]
        elif grid[1][2] != "X":
            grid[1][1] = grid[1][2]
        elif grid[1][0] != "X":
            grid[1][1] = grid[1][0]
        else:
            if grid[0][2] != "X" and grid[2][0] != "X":
                grid[1][1] = ((grid[0][2] - grid[2][0]) // 2) + grid[0][2]
            else:
                grid[1][1] = ((grid[2][2] - grid[0][0]) // 2) + grid[0][0]
            xCount -= 1
            rowXCount[1] -= 1
            columnXCount[1] -= 1
            sixX()
            return
        xCount -= 1
        rowXCount[1] -= 1
        columnXCount[1] -= 1
    else:
        grid[2][1] = grid[1][1]
        grid[0][1] = grid[1][1]
        xCount -= 2
        rowXCount[0] -= 1
        rowXCount[2] -= 0
        columnXCount[1] = 0

    fillRowsAndColumns()


def fillRowsAndColumns():
    if xCount > 0:
        for i in range(3):
            fillRow(i)
            fillColumn(i)
        if xCount == 4:
            fourX()
        if xCount <= 5:
            fillRowsAndColumns()
    # main


def main():
    global grid
    # fill in rows with 2 items
    if xCount == 9:
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    elif xCount == 8:
        value = None
        for i in range(3):
            for j in range(3):
                if grid[i][j] != "X":
                    value = grid[i][j]
        grid = [[value, value, value], [
            value, value, value], [value, value, value]]
    else:
        fillRowsAndColumns()
        if xCount > 0:
            if xCount <= 4:
                fourX()
            elif xCount == 6:
                sixX()
            elif xCount == 7:
                sevenX()


main()
for row in grid:
    result = [str(i) for i in row]
    print(" ".join(result))
