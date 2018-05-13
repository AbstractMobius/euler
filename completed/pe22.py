import re
import string

char_vals = {string.ascii_lowercase[i]:i+1 for i in range(len(string.ascii_lowercase))}

summation = 0
with open("p022_names.txt") as f:
    names = re.findall(r'"(.*?)"', f.read().lower())
names = sorted(names)
for i in range(len(names)):
    for k in names[i]:
        summation += char_vals[k]*(i+1)
print(summation)