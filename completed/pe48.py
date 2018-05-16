summation = 0
for i in range(1,1001):
    summation += i**i
print(summation%10**10)