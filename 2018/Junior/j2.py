length = int(input())
yesterday = input()
today = input()

counter = 0
for i in range(length):
    if yesterday[i] == today[i] == "C":
        counter = counter + 1

print(counter)


