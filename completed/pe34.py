import math


r_func = list(range(10**7)) # lets just check a ton of numbers lol

for i in r_func:
    if i == int(sum([math.factorial(int(k)) for k in str(i)])):
        print(i)




