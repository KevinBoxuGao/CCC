gridDimensions = input().split()
N = int(gridDimensions[0])
W = int(gridDimensions[1])

grid = []
points = []
sCoord = []
cameras = []

# setup grid
for i in range(N):
    row = input()
    grid.append([])
    for j in range(len(row)):
        grid[i].append(row[j])
        if grid[i][j] == 'S':
            sCoord = [i, j]
        elif grid[i][j] == '.':
            points.append([i, j])
        elif grid[i][j] == 'C':
            cameras.append([i, j])

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

visited = []
nodes_in_next_layer = 0

# mark nonvalid camera spaces
for coord in cameras:
    for i in range(4):
        r = coord[0]
        c = coord[1]
        while grid[r][c] != "W":
            cell = grid[r][c]
            if cell == ".":
                grid[r][c] = 'X'
            r += dr[i]
            c += dc[i]


def explore_node(r, c):
    global rq, cq, nodes_in_next_layer, visited
    if visited[r][c] == True:
        return
    visited[r][c] = True
    cell = grid[r][c]
    if cell == "X":
        return
    elif cell == "W":
        return
    elif cell == "C":
        return
    else:
        if cell == "." or cell == "S":
            rq.append(r)
            cq.append(c)
            nodes_in_next_layer += 1
        else:
            if cell == "L":
                rr = r + dr[3]
                cc = c + dc[3]
            elif cell == "R":
                rr = r + dr[2]
                cc = c + dc[2]
            elif cell == "U":
                rr = r + dr[0]
                cc = c + dc[0]
            else:
                rr = r + dr[1]
                cc = c + dc[1]
            explore_node(rr, cc)


def explore_neighbours(r, c):
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        explore_node(rr, cc)


def shortestPath(start, end):
    # start coord
    sr = sCoord[0]
    sc = sCoord[1]
    # dot coord
    er = start[0]
    ec = start[1]

    # queue
    global rq, cq, nodes_in_next_layer, visited
    rq = [sr]
    cq = [sc]

    move_count = 0
    nodes_in_layer = 1
    nodes_in_next_layer = 0

    reached_end = False

    visited = []
    for row in range(N):
        visited.append([])
        for col in range(W):
            visited[row].append(False)

    visited[sr][sc] = True

    # BFS for finding shortest path
    while len(rq) > 0:
        r = rq.pop(0)
        c = cq.pop(0)
        if r == er and c == ec:
            reached_end = True
            break
        explore_neighbours(r, c)
        nodes_in_layer -= 1
        if nodes_in_layer == 0:
            nodes_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1
    if reached_end:
        return move_count
    return -1


results = []
# find smallest paths
for coord in points:
    r = coord[0]
    c = coord[1]
    # camera watched square
    if grid[r][c] == "X":
        results.append(-1)
        continue
    # find shortest path
    results.append(shortestPath(coord, sCoord))

for i in results:
    print(i)
