a = set()
for i in range(2,101):
    for k in range(2, 101):
        a.add(i**k)
print(len(a))

b = set()
b.add(1)
b.add(1)
print(len(b))

