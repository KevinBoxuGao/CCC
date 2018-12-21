import math
def returnSumDivs(num):
    sumn = 0
    for i in range(1, math.ceil(num/2)+1):
        if (num/i).is_integer() == True:
            sumn += i
    return sumn
