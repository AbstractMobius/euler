
def factors(n):
    #https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    return set(x for tup in ([i, n//i]
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

factor_sums = {}
for k in range(1, 10000):
    factor_sums[k] = sum(list(factors(k)))-k

summation = 0
for key in factor_sums:
    key = key # just for clarification
    value = factor_sums[key]
    try:
        if factor_sums[value] == key and value != key:
            summation += value
    except KeyError:
        pass

print(summation) # because we add them twice :3