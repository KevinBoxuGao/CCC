class edge:
    def __init__(self, a, b, c, original):
        self.v1 = a
        self.v2 = b
        self.weight = c
        self.original = original


# input
n, m, d = [int(i) for i in input().split()]
edges = []
# valid plan
for i in range(n-1):
    a, b, c = [int(i) for i in input().split()]
    edges.append(edge(a, b, c, True))
# inactive pipes
for i in range(m-n+1):
    a, b, c = [int(i) for i in input().split()]
    edges.append(edge(a, b, c, False))

# disjoined set to find cycle
parent = (n+1)*[-1]


def find(edge):
    if parent[edge] == -1:
        return edge
    if parent[edge] != -1:
        return find(parent[edge])


def connected(x, y):
    return find(x) == find(y)


def union(edge1, edge2):
    set_1 = find(edge1)
    set_2 = find(edge2)
    parent[set_1] = set_2


def KruskalMST():
    edges.sort(key=lambda x: x.weight)
    days = 0
    newOriginal = m*[False]

    maxWeight = 0
    numEdges = 0
    for i, edge in enumerate(edges):
        if numEdges == (n - 1):
            break

        if connected(edge.v1, edge.v2) == False:
            maxWeight = edge.weight
            numEdges += 1
            union(edge.v1, edge.v2)
            newOriginal[i] = True
            if edge.original != True:
                days += 1

    if d > 0:
        numEdges = 0
        global parent
        parent = (n+1)*[-1]
        for i, edge in enumerate(edges):
            if numEdges == (n - 1):
                break
            if connected(edge.v1, edge.v2) == False:
                if edge.weight < maxWeight or (edge.weight == maxWeight and edge.original):
                    union(edge.v1, edge.v2)
                    numEdges += 1
                elif(edge.original and edge.weight <= d):
                    print(days - 1)
                    return
    print(days)


KruskalMST()
