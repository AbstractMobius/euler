

print(6952+7852+5796+5346+4396+7254)

summation = 0
prods = []
for i in range(2000):
    for k in range(2000):
        v = [int(j) for j in str(i*k) + str(i) + str(k)]
        if sum(v) == 45 and len(v) == 9 \
                and len(set(v)) == 9 and sorted([i,k])\
                not in prods:
            print(sorted(v), i*k)
            summation += i*k
            prods.append(sorted([i,k]))

print(summation)



