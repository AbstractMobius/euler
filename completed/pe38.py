
r_range = list(range(1, 10000))

def has_repeating_digits(num):
    a = [i for i in str(num)]
    return not len(a) == len(set(a))

def is1to9Pandigital(num):
    a = [i for i in str(num)]
    return len(a) == 9 == len(set(a)) and '0' not in a

summation = 0
pandigitals = []

for number in r_range:
    if not has_repeating_digits(number):
        s = ""
        itr = 1
        while len(s) < 9:
            s += str(number*itr)
            itr += 1
        if len(s) == 9 and is1to9Pandigital(s):
            pandigitals.append(int(s))

print(sorted(pandigitals, reverse=True))
