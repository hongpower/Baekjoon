# 평균은 넘겠지
c = int(input())
for _ in range(c):
    lst = list(map(int,input().split()))
    stuN = len(lst)-1
    avg = (sum(lst)-lst[0])/stuN
    passN = 0
    for i in lst[1:]:
        if i > avg :
            passN += 1
    print('{:.3f}%'.format(round((passN/stuN)*100,ndigits=3)))
