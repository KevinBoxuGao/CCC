x = []
for i in range(4):
    x.append(int(input()))

if x[1] == x[2]:
    if x[0] == 8:
        if x[3] == 8:
            print("ignore")
        elif x[3] == 9:
            print("ignore")
        else:
            print("answer")
    elif x[0] == 9:
        if x[3] == 8:
            print("ignore")
        elif x[3] == 9:
            print("ignore")
        else:
            print("answer")
    else:
        print("answer")
else:
    print("answer")
