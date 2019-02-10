pages = int(input())
access = list(range(2,pages+1))
shortest = 0
p = 1

data = [0]

for i in range(1,pages+1):
    temp = [int(x) for x in input().split(" ")]
    if temp[0] == 0:
        data.append(0)
    else:
        data.append(temp[1:])
    if temp[0] not in access:
        for j in range(1,temp[0]+1):
            if temp[j] in access:
                access.remove(temp[j])
        
if not access:
    print("Y")
else:
    print("N")

def shortestPath():



print(shortest)