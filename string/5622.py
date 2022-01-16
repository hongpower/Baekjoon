# 다이얼
alpha = list(input())
alphag = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO','PQRS', 'TUV', 'WXYZ']
alpha2lst = []

## 2차원 리스트 생성 (굳이 만들필요 X)
for a in alphag:
    lst = []
    for i in a:
        lst.append(i)
    alpha2lst.append(lst)

dtime = 0
for a in alpha: # 입력 알파벳의 각 문자
    for i in alpha2lst: # 리스트내의 리스트
        if a in i:
            dtime += alpha2lst.index(i) + 3 # 인덱스의 +3만큼 시간이 걸림

print(dtime)
