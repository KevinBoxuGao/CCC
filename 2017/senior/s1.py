games = int(input())

s1 = [int(i) for i in input().split()]
s2 = [int(i) for i in input().split()]

maxSum = 0

sum1 = 0
sum2 = 0

for i in range(games):
    sum1 += s1[i]
    sum2 += s2[i]
    if sum1 == sum2:
        maxSum = i + 1

print(maxSum)
