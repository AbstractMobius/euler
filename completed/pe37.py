from tools import isPrime


summation = 0
r_onemil = list(range(10, 1000000))
for i in r_onemil:
    s = ""
    for k in str(i):
        s += k
        if s=='1' or not isPrime(int(s)):
            break
        if int(s)==i:
            s1 = ""
            for j in str(i)[::-1]:
                s1 = j + s1
                if s1 == '1' or not isPrime(int(s1)):
                    break
                if int(s1) == i:
                    summation += i
print(summation)
