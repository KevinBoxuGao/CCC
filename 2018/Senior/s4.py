weight = int(input())

subTrees = (weight+1)*[0]
subTrees[1] = 1
subTrees[2] = 1
subTrees[3] = 2
subTrees[4] = 3
subTrees[5] = 4

def findNumberOfSubTrees(n):
    possibilities = 0
    for i in range(2, n+1):
        subtreeWeight = n//i
        if subTrees[subtreeWeight] != 0:
            possibilities += subTrees[subtreeWeight]
        else:
            findNumberOfSubTrees(subtreeWeight)
            possibilities += subTrees[subtreeWeight]
    subTrees[n] = possibilities

if weight > 4:
    findNumberOfSubTrees(weight)

print(subTrees[weight])