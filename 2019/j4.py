grid = [['1','2'],['3','4']]

s = input()
v = 0
h = 0
for i in s:
    if i == "V":
        v = v + 1
    else:
        h = h + 1

if h % 2 != 0:
    grid[0][0], grid[1][0] = grid[1][0], grid[0][0]
    grid[0][1], grid[1][1] = grid[1][1], grid[0][1]
    
if v % 2!=0:
    grid[0][0], grid[0][1] = grid[0][1], grid[0][0]
    grid[1][0], grid[1][1] = grid[1][1], grid[1][0]



print(" ".join(grid[0]))
print(" ".join(grid[1]))