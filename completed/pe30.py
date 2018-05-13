
print(4150+\
4151+\
54748+\
92727+\
93084)



for i in range(0,10): #wont be greater than 9**5==59049 aka five digits
    for j in range(0,10):
        if i**5+j**5==int(str(i) + str(j)):
            print(i+j)
        for k in range(0,10):
            if i**5+j**5+k**5==int(str(i) + str(j) + str(k)):
                print(i+j+k)
            for l in range(0,10):
                if i**5+j**5+k**5+l**5==int(str(i) + str(j) + str(k) + str(l)):
                    print(i,j,k,l)
                for m in range(0,10):
                    if i**5+j**5+k**5+l**5+m**5==int(str(i)+str(j)+str(k)+str(l)+str(m)):
                        print(i,j,k,l,m)
                        for n in range(0, 10):
                            if i ** 5 + j ** 5 + k ** 5 + l ** 5 + m ** 5+ n ** 5 == int(
                                    str(i) + str(j) + str(k) + str(l) + str(m)+ str(n)):
                                print(i, j, k, l, m,n)



