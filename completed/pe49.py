from tools import isPrime

primes = [i for i in range(1000, 10000) if isPrime(i)]

for i in range(1000, 10000):
    for k in primes:
        if isPrime(k) and isPrime(k+i) and isPrime(k+(i*2)):
            a,b,c = [i for i in str(k+i)],\
                    [i for i in str(k+(i*2))], [i for i in str(k+(i*3))]
            if sorted(a)==sorted(b)==sorted(c):
                print(a,b,c)





