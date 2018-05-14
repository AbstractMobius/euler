import math

# all of these are things I wrote in my pe(n) files, that I later needed to re-use


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

def isPalindromic(str_num):
    return str_num[:int(math.floor(len(str_num)/2))] == str_num[int(math.ceil(len(str_num)/2)):][::-1]

def has_repeating_digits(num):
    a = [i for i in str(num)]
    return not len(a) == len(set(a))

def is1to9Pandigital(num):
    a = [i for i in str(num)]
    return len(a) == 9 == len(set(a)) and '0' not in a

