from tools import isPrime
primes = [[int(k) for k in str(i)] for i in range(1,100000) if isPrime(i)]

for i in range(5):
    p = [k for k in primes if len(k)==i+1]
    for j in range(i):
        g = []
        for item in p:
            try:
                item.pop(j);item.pop(-1)
                g.append(item)
            except Exception:
                pass
        for m in g:
            if g.count(m)==8:
                print(m,j)
                break








