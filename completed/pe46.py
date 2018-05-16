from tools import isPrime

primes = [i for i in range(2,10000) if isPrime(i)]
non_primes = [i for i in range(2,10000) if not isPrime(i)]

def find():
    for np in non_primes:
        hit = False
        for p in primes:
            if hit:
                break
            if p > np:
                if np%2 == 1:
                    print(np)
                    return
                break
            for i in range(1,100):
                val = p+2*i**2
                if val == np:
                    hit = True
                    break
                elif val > np:
                    break
find() # needed to do method b/c return




