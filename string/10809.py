# 알파벳 찾기
s = list(i for i in input()) # 입력값 리스트
lst = list(a for a in 'abcdefghijklmnopqrstuvwxyz') # 알파벳 리스트

for i in range(len(lst)):
    if lst[i] in s: # 만약 알파벳리스트의 i번째 알파벳이 s에 있다면
        print(s.index(lst[i]),end=' ') # 해당 알파벳의 s 안에 위치(인덱스) 출력
    else:
        print(-1,end=' ') # 없다면 -1 출력


