import re
import string

char_vals = {string.ascii_lowercase[i]:i+1 for i in range(len(string.ascii_lowercase))}

with open("p042_words.txt") as f:
    a = re.findall(r'"(.*?)"', f.read().lower())

triangle_numbers = []
for i in range(1,10000):
    triangle_numbers.append(int(0.5*i*(i+1)))

summation = 0
for i in range(len(a)):
    val = 0
    for k in a[i]:
        val += char_vals[k]
    if val in triangle_numbers:
        summation+=1

print(summation)