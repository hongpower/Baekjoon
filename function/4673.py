# 셀프 넘버 : 개어려움
lst = [i for i in range(10001)]
lst2 = []
for one in range(10):
    a = one
    for two in range(10):
        b = two
        for three in range(10):
            c = three
            for four in range(10):
                d = four
                lst2.append(a + b + c + d + (a*1000+b*100+c*10+d))

for i in sorted(lst2):
    if i in lst:
        lst.remove(i)

for i in lst:
    print(i)

