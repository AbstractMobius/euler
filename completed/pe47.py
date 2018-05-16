from tools import isPrime

primes = [i for i in range(2,100000) if isPrime(i)]
non_primes = [i for i in range(2,1000000) if not isPrime(i)]

def num_unique_prime_factors(n, f=list()):
    for p in primes:
        if p>n:
            return 0
        elif n%p==0:
            if n/p!=1.0:
                if p in f:
                    return 0 + num_unique_prime_factors(n / p, f)
                else:
                    return 1 + num_unique_prime_factors(n/p, f+[p])
            else:
                if p not in f:
                    return 1
                else:
                    return 0
l = list()
t1 = False
t2 = False
t3 = False
t4 = False
for i in non_primes:
    upf = num_unique_prime_factors(float(i))
    if upf == 4 and not t1:
        t1 = True
        l.append(i)
    elif upf == 4 and t1 and not t2:
        t2 = True
        l.append(i)
    elif upf == 4 and t1 and t2 and not t3:
        t3 = True
        l.append(i)
    elif upf == 4 and t1 and t2 and t3 and not t4:
        l.append(i)
        print(l)
    else:
        l.clear()
        t1,t2,t3=False,False,False




