x = input()
y = input()

def divisible_by_11(a):
    b = int(two_digits(a))
    if b % 11 == 0:
        print("The number", a, "is divisible by 11.")
    else:
        print("The number", a, "is not divisible by 11.")

def two_digits(a):
    if len(a) <= 1:
        return a
    else:
        print(a)
        return two_digits(str(int(a[:len(a)-1]) - int(a[len(a)-1]))) 

for i in y.split():
    divisible_by_11(i)


