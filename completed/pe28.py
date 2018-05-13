

summation = 1
for i in range(1001, 1, -2):
    for k in range(4):
        summation+= i**2-(i-1)*k
# programming is a tool, math is an art -samuel schmidgall
print(summation)
