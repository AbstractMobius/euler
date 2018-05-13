import math

def factors(n):
    #https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    return set(x for tup in ([i, n//i]
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

#note - only works <= 10^9
def isPrime(x):
    #http://code.activestate.com/recipes/578402-effcient-prime-number-generator-in-python/
    z=True
    for i in range(2,x):
        if i<=math.sqrt(x):
            if x%i!=0:
                z=True
            else:
                z=False
                break
        else:
            break
    return z

