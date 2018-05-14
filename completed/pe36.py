from tools import isPalindromic


summation = 0
r_onemil = list(range(1, 1000000))
for i in r_onemil:
    if isPalindromic(str(i)) and isPalindromic(bin(i)[2:]):
        summation+=i
print(summation)



