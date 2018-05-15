def is0to9Pandigital_and_special(num):
    rr = [None, 2, 3, 5, 7, 11, 13, 17]
    b = [v for v in str(num)]
    s = str(num)
    if len(b) == 10 == len(set(b)):
        for bb in range(1,8):
            if not int(s[bb:bb+3])%rr[bb] == 0:
                return False
        return True
    return False

summation = 0
for i in reversed(range(10)):
    i1 = [k for k in reversed(range(10)) if k!=i]
    for j in i1:
        i2 = [k for k in reversed(range(10)) if k != i and k!=j]
        for j1 in i2:
            i3 = [k for k in reversed(range(10)) if k != i and k != j  and k != j1]
            for j2 in i3:
                i4 = [k for k in reversed(range(10)) if k != i and k != j and k != j1 and k != j2]
                for j3 in i4:
                    i5 = [k for k in reversed(range(10)) if k != i and k != j  and k != j1 and k != j2 and k != j3]
                    for j4 in i5:
                        i6 = [k for k in reversed(range(10)) if k != i and k != j and k != j1 and k != j2 and k != j3 and k != j4]
                        for j5 in i6:
                            i7= [k for k in reversed(range(10)) if k != i and k != j and k != j1 and k != j2 and k != j3 and k != j4 and k!=j5]
                            for j6 in i7:
                                i8 = [k for k in reversed(range(10)) if k != i and k != j and k != j1 and k != j2 and k != j3 and k != j4 and k != j5 and k != j6]
                                for j7 in i8:
                                    i9 = [k for k in reversed(range(10)) if k != i and k != j and k != j1 and k != j2 and k != j3 and k != j4 and k != j5 and k != j6 and k != j7]
                                    a = int(str(i) + str(j) + str(j1) + str(j2) + str(j3) + str(j4)\
                                                 + str(j5)+ str(j6)+ str(j7)+ str(i9[0]))
                                    if is0to9Pandigital_and_special(a):
                                        summation+=int(a)
print(summation)