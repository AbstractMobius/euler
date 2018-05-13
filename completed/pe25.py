

f1 = 1
f2 = 1
itr = 2
while len(str(f1)) != 1000:
    itr += 1
    temp = f1
    f1 = f1 + f2
    f2 = temp
print(itr)


