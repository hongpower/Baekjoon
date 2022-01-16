# 그룹 단어 체커
n = int(input())
cnt = n
for _ in range(n):
    word = input()
    for w in range(len(word)-1):
        if word[w] == word[w+1]:
            pass
        elif word[w] in word[w+1:]: # 알파벳이 존재하는데 바로 다음에가 아니라면
            cnt -=1
            break
print(cnt)

