n = int(input())
lengthFrequencies = 2002*[0]
sumFrequencies = 4001*[0]

for i in input().split():
    lengthFrequencies[int(i)] += 1


def naive():
    maxLength = 0
    possibleLengths = 0

    for i in range(1, 2001):
        if lengthFrequencies[i] == 0:
            continue
        else:
            for j in range(i, 2001):
                if i == j:
                    sumFrequencies[i + j] += lengthFrequencies[i] // 2
                else:
                    boardSum = i + j
                    sumFrequencies[boardSum] += min(
                        lengthFrequencies[i], lengthFrequencies[j])

    for i in range(4001):
        if sumFrequencies[i] > maxLength:
            maxLength = sumFrequencies[i]
            possibleLengths = 1
        elif sumFrequencies[i] == maxLength:
            possibleLengths += 1

    print(str(maxLength) + " " + str(possibleLengths))


naive()
