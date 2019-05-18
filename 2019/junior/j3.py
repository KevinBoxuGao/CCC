n = int(input())

for i in range(n):
    output = []
    x = input()
    char = x[0]
    counter = 0
    for i in range(len(x)):        
        if i == len(x)-1:
            if char == x[i]:
                counter = counter + 1
                output.append(str(counter) + " " + char)
            else:
                output.append(str(counter)+" "+char)
                output.append("1 "+x[i])
        elif char == x[i]:
            counter = counter + 1
        else:
            output.append(str(counter) + " " + char)
            char = x[i]
            counter = 1
    print(" ".join(output))