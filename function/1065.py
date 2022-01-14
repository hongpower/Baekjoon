# 한수
cnt = 0
n = int(input())

for i in range(1,n+1):
    lst = list(map(int,str(i)))
    lenN = len(lst)
    if lenN == 1 or lenN ==2:
        cnt += 1
    else:
        diff1 = lst[2]-lst[1]
        diff2 = lst[1]-lst[0]
        if diff1 == diff2:
            cnt += 1

print(cnt)
