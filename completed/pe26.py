from decimal import Decimal, getcontext

getcontext().prec = 5000

def repeat_size(n):
    for k in range(2500):
        rec_s = n[k]
        itr = k
        while itr < len(n)-1:
            itr += 1
            if rec_s == n[itr:itr+len(rec_s)]:
                if rec_s == n[itr*2:itr*2+len(rec_s)]: # pattern repeats
                    return itr
            rec_s += n[itr]
    b = len(n)
    print()

maxx = 0
ind = 0
unit = Decimal(1)
for i in range(2, 1000):
    dec = str(unit/Decimal(i))[2:]
    if len(dec) == 5002:
        a = repeat_size(dec)
        if a is not None and a >= maxx:
            maxx = a
            ind = i
print(ind, maxx)