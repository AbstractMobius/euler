import math
right_tri_perim = lambda a,b: a+b+math.sqrt(a**2+b**2)

maxx = 0
ind = 0
for j in range(1, 1001):
    num = 0
    for i in range(1, j):
        for k in range(i, j):
            if right_tri_perim(i,k) == float(j):
                num += 1
    if num > maxx:
        maxx = num
        ind = j
print(ind)



