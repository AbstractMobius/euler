goal = 200
items = list(reversed([1, 2, 5, 10, 20 ,50, 100]))

# et tu brute force?
summation = 0
for i in range(0, goal, items[0]):
    for j in range(0,goal, items[1]):
        for k in range( 0,goal, items[2]):
            for l in range( 0,goal, items[3]):
                for m in range( 0,goal, items[4]):
                    for n in range( 0,goal, items[5]):
                        for o in range( 0,goal, items[6]):
                            if i+j+k+l+m+n+o == goal:
                                summation+=1


print(summation+8)



