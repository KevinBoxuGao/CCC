import math
a=[]

inputs = int(input())

for i in range(0 ,inputs):
    n = int(input())
    a.append(n)

outputs= []
def returnSumDivs(num):
    sumn = 0
    for i in range(1, math.ceil(num/2)+1):
        if (num/i).is_integer() == True:
            sumn += i
    if sumn == num:
        outputs.append(str(num)+' is a perfect number')
    elif sumn > i:
        outputs.append(str(num)+' is an abundant number')
    else:
        outputs.append(str(num)+' is a deficient number')

for each in a:
    returnSumDivs(each)
          
for i in outputs:
    print(i)
