import math
comb = lambda n,r:math.factorial(n)//(math.factorial(r)*math.factorial(n-r))

summation = 0
for i in range(1,101):
    for k in range(1,i):
        if comb(i, k) >= 1000000:
            summation +=1
print(summation)






