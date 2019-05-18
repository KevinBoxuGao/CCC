points = []

#input 
N = int(input())
for i in range(N):
    points.append(int(input()))

points.sort()
sizes = []
for i in range(1,N-1):
    left = (points[i] - points[i-1])/2
    right = (points[i+1] - points[i])/2

    sizes.append(left + right)

print(min(sizes))