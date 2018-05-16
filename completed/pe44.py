pentag_nums = lambda n:(n*(3*n-1))/2
pent = [pentag_nums(i) for i in range(1000,10000)]

for i in pent:
    for k in pent:
        if i != k and i+k in pent and abs(i-k) in pent:
            print(i,k)










