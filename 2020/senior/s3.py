import copy 

N = input()
M = input()

value = 0
frequencies = {}
subStrings = set()

for char in N:
    if char in frequencies:
        frequencies[char] += 1
    else:
        frequencies[char] = 1

#generate substrings
def generateSubString(current, values):
    if len(current) == len(N):
        if current in subStrings:
            return
        else:
            subStrings.add(current)
            return
    else:
        for k in values:
            if values[k] > 0:
                nextCurrent = current + k
                copied = copy.deepcopy(values)
                copied[k] -= 1
                generateSubString(nextCurrent, copied)
            else:
                continue


generateSubString("", frequencies)    


#check for substring
for subString in subStrings:
    if subString in M:
        value += 1

print(value)