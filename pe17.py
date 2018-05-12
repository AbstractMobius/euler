layer1={1:len("one"),2:len("two"),3:len("three"),4:len("four"),5:len("five"),6:len("six"),7:len("seven"),8:len("eight"),9:len("nine")}
layer10_19={10:len("ten"),11:len("eleven"),12:len("twelve"),13:len("thirteen"),14:len("fourteen"),15:len("fifteen"),16:len("sixteen"),17:len("seventeen"),18:len("eighteen"),19:len("nineteen")}
layer2={2:len("twenty"),3:len("thirty"),4:len("fourty"),5:len("fifty"),6:len("sixty"),7:len("seventy"),8:len("eighty"),9:len("ninety")}
layer3={1:len("onehundred"),2:len("twohundred"),3:len("threehundred"),4:len("fourhundred"),5:len("fivehundred"),6:len("sixhundred"),7:len("sevenhundred"),8:len("eighthundred"),9:len("ninehundred")}

summation = 0
for i in range(1, 1000):
    if i<10:
        summation+=layer1[i]
    elif i < 20:
        summation+=layer10_19[i]
    elif i<100:
        summation+=layer2[i//10]
        if i%10!=0:summation+=layer1[i%10]
    elif i<1000:
        if i%100 in range(10,20):
            summation+=3
            summation+=layer10_19[i%100]
            summation+=layer3[i//100]
        else:
            summation+=layer3[i//100]
            if i%100//10!=0 or i%10!=0:summation+=3 # for the and
            if i%100//10!=0:summation+=layer2[(i%100)//10]
            if i%10!=0:summation+=layer1[i%10]
print(summation+len("onethousand"))