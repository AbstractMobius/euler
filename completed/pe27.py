from tools import isPrime
print(-61*971)
primes = []
for i in range(1,1000): # b has to be prime and > 0
    if isPrime(i):
        primes.append(i)
# if a < 0 then a*39+b>0 because a=1,b=40 == 39
max_seq = 0
t,v=0,0
for a in range(-1000, 1000):
    for b in primes:
        n = 0
        seq = 0
        c=n**2+a*n+b
        while 0 < c == abs(c) and isPrime(c):
            seq+=1
            n+=1
            c=n**2+a*n+b
        if seq>max_seq:
            max_seq = seq
            t=a
            v=b
        print(a)

print(t,v)

