from tools import isPrime

numbers = list(range(2,10**6))

summation = 0
for number in numbers:
    n = str(number)
    ln = len(n)
    g = True
    for start_digit in range(ln):
        v = ""
        for d in range(ln):
            v += n[(start_digit+d)%ln]
        if not isPrime(int(v)):
            g=False
            break
    if g:
        summation+=1

print(summation)

