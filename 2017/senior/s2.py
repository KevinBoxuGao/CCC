n = int(input())
measurements = [int(i) for i in input().split()]
measurements.sort()


def order():
    if n == 1:
        print(measurements[0])
        return

    if n % 2 == 0:
        middle = (n // 2)
    else:
        middle = (n // 2) + 1

    lower = measurements[:middle]
    lowerLen = len(lower)
    higher = measurements[middle:]
    higherLen = len(higher)
    result = []

    i = lowerLen - 1
    j = 0

    while i >= 0 and j < higherLen:
        result.append(lower[i])
        result.append(higher[j])
        i -= 1
        j += 1

    if lowerLen != higherLen:
        if n % 2 == 0:
            result.append(higher[-1])
        else:
            result.append(lower[0])

    print(*result)


order()
