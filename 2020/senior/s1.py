n = int(input())
speeds = []
for i in range(n):
    speeds.append([int(i) for i in input().split()])
speeds = sorted(speeds, key=lambda speed: speed[0])

value = 0
for i in range(len(speeds)-1):
    diffPosition = abs(speeds[i][1] - speeds[i+1][1])
    diffTime = speeds[i+1][0] - speeds[i][0]
    velocity = diffPosition / diffTime
    if velocity > value:
        value = velocity

print(value)
