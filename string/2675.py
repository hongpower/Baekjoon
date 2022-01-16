# 문자열 반복
t = int(input())
for _ in range(t):
    r, s = input().split()
    for i in range(len(s)):
        print(s[i] * int(r),end='')
    print() # 한 반복문이 끝나면 줄을 바꿔서 할 수 있도록