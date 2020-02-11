N = int(input())
frequencies = 1001*[0]
for i in range(N):
    frequencies[int(input())] += 1

largest = max(frequencies)
firstNumbers = []
secondLargest = 0
secondNumbers = []

for i in range(1, 1001):
    if frequencies[i] == 0:
        continue
    elif frequencies[i] == largest:
        firstNumbers.append(i)
    elif frequencies[i] > secondLargest and frequencies[i] < largest:
        secondLargest = frequencies[i]

for i in range(1, 1001):
    if frequencies[i] == secondLargest:
        secondNumbers.append(i)


if len(firstNumbers) == 1 and len(secondNumbers) == 1:
    value = abs(firstNumbers[0] - secondNumbers[0])
    print(value)
elif len(firstNumbers) > 1:
    value = abs(max(firstNumbers) - min(firstNumbers))
    print(value)
elif len(firstNumbers) == 1 and len(secondNumbers) > 1:
    first = firstNumbers[0]
    maxSecond = max(secondNumbers)
    minSecond = min(secondNumbers)
    value1 = abs(first - maxSecond)
    value2 = abs(first - minSecond)
    value = max([value1, value2])

    print(value)
