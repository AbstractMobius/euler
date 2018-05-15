from tools import isPrime
m=0
def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
        return False
    return True

for i in reversed(range(1,8)):
    i1 = [k for k in reversed(range(1,8)) if k!=i]
    for j in i1:
        i2 = [k for k in reversed(range(1, 8)) if k != i and k!=j]
        for j1 in i2:
            i3 = [k for k in reversed(range(1, 8)) if k != i and k != j  and k != j1]
            for j2 in i3:
                i4 = [k for k in reversed(range(1, 8)) if k != i and k != j and k != j1 and k != j2]
                for j3 in i4:
                    i5 = [k for k in reversed(range(1, 8)) if k != i and k != j  and k != j1 and k != j2 and k != j3]
                    for j4 in i5:
                        i6 = [k for k in reversed(range(1, 8)) if k != i and k != j and k != j1 and k != j2 and k != j3 and k != j4]
                        a = int(str(i) + str(j) + str(j1) + str(j2) + str(j3) + str(j4)\
                                 + str(i6[0]))

                        if is_prime_number(a):
                            print(a)
print(m)




