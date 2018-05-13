from tools import factors


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