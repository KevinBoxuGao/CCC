rules = []
for i in range(3):
    rules.append(input().split(" "))

rule = input().split(" ")

S = int(rule[0])
I = rule[1]
F = rule[2]


def substrings(substring, characters, result):
    x = characters.find(substring)
    if x == -1:
        return
    else:
        result.append(x)
        substrings(substring, characters[x:], result)

def possibilities(characters):
    outputs = []
    for i in range(3):
        results = []
        if rules[i][0] in characters:
            substrings(rules[i][0], characters, results)
            for i in results:
                outputs.append()
        else:
            continue
    
    return(outputs)

for i in range(3):
    if rules[i][0] in characters:
        x = I.find(rules[i][0])
        I[x:x+len(rules[i][0])]
    else:
        continue

for i in range(S):
    print(rule number, index, result)






