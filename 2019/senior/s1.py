sequence = str(input())
v = sequence.count("V") % 2
h = sequence.count("H") % 2

if v == 1 and h == 1:
    print("4 3")
    print("2 1")
elif v == 1:
    print("2 1")
    print("4 3")
elif h == 1:
    print("3 4")
    print("1 2")
else:
    print("1 2")
    print("3 4")
