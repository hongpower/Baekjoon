# 크로아티아 알파벳

lst = ['c=','c-','dz=','d-','lj','nj','s=','z=']
alpha = list(input())
cnt = 0
n = 0

while True:
    # if n > len(alpha): #9
    #     break

    if n == len(alpha):
        break

    if n == len(alpha)-1:
        cnt += 1
        break

    twonum = alpha[n] + alpha[n + 1]

    if twonum == 'dz' and (len(alpha)-n) > 2:
        if alpha[n+2] == '=':
            cnt += 1
            n += 3
        else:
            cnt += 1
            n += 1
    else:
        if twonum in lst:
            cnt += 1
            n += 2
        else:
            cnt += 1
            n += 1

print(cnt)

## 다른 사람들꺼 참고해서 하는 간단한 코드
croatialst = ['c=','c-','dz=','d-','lj','nj','s=','z=']
letter = input()

for i in croatialst:
    letter.replace(i,'o')

print(len(letter))