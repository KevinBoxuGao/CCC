y = [0] + input().split(" ")
x = [int(z) for z in y]

for i in range(len(x)):
    position = sum(x[:i+1])
    output = []
    for j in range(len(x)):
        output.append(abs(position - sum(x[:j+1])))
    print(" ".join(str(x) for x in output))

