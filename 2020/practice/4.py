M = int(input())
# input
borders = {}
edges = []
graphNoBorders = []
# all connections
for vertex in range(M):
    row = [int(i) for i in input().split()]
    numWalls = row[0]
    for pair in range(1, numWalls + 1):
        weight = row[numWalls + pair]
        if pair == numWalls:
            try:
                borders[(row[pair], row[1], weight)].append(vertex+1)
            except:
                try:
                    borders[(row[1], row[pair], weight)].append(vertex+1)
                except:
                    borders[(row[pair], row[1], weight)] = [vertex+1]
        else:
            try:
                borders[(row[pair], row[pair+1], weight)].append(vertex+1)
            except:
                try:
                    borders[(row[pair+1], row[pair], weight)].append(vertex+1)
                except:
                    borders[(row[pair], row[pair+1], weight)] = [vertex+1]
# makes edges
for k, v in borders.items():
    if len(v) == 1:
        edges.append([v[0], 0, k[2]])
    elif len(v) > 1:
        edges.append([v[0], v[1], k[2]])

# graphs
for edge in edges:
    if edge[1] == 0:
        continue
    else:
        graphNoBorders.append(edge)

# MST


def find(parents, x):
    if parents[x] == -1:
        return x
    else:
        return find(parents, parents[x])


def union(parents, x, y):
    xParent = find(parents, x)
    yParent = find(parents, y)

    parents[xParent] = yParent


def MST(graph):
    cost = 0
    edges = sorted(graph, key=lambda weight: weight[2])
    parent = (len(graph) + 1)*[-1]
    for edge in edges:
        xParent = find(parent, edge[0])
        yParent = find(parent, edge[1])
        if xParent != yParent:
            union(parent, xParent, yParent)
            cost += edge[2]

    return cost


def main():
    result1 = MST(edges)
    result2 = MST(graphNoBorders)
    print(min(result1, result2))


main()
