games = int(input())
s1 = [int(i) for i in input().split()]
s2 = [int(i) for i in input().split()]


def largestDay(s1, s2):
    sum1 = 0
    sum2 = 0
    maxDay = None

    for i in range(games):
        sum1 += s1[i]
        sum2 += s2[i]
        if sum1 == sum2:
            maxDay = i

    if maxDay != None:
        return maxDay + 1
    return 0


def main():
    print(largestDay(s1, s2))


main()
