import math
from tools import factors, isPrime

def proper_divisors_sum(n):
    return sum(factors(n))-n

abundant_nums = []
summation = 0
for i in range(1,28124): # find all abundant numbers
    if i < proper_divisors_sum(i):
        abundant_nums.append(i)


def sum_of_abundant(n):
    for k in range(len(abundant_nums)):
        if abundant_nums[k]+abundant_nums[k] < n: # lower bound
            pass
        else:
            if abundant_nums[k] > n: # upper bound
                return True
            for j in range(1,k):
                if abundant_nums[j] > n: # upper bound
                    break
                if abundant_nums[k]+abundant_nums[j]==n:
                    return False
    return True


for i in range(1,28124):
    if not isPrime(i) and sum_of_abundant(i):
        summation += i
print(summation)


