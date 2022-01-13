# OX 퀴즈
n = int(input())
for case in range(n):
    test = input()
    s = 0
    score = 0
    for i in test:
        if i == 'O':
            s += 1
            score += s
        else:
            s = 0
    print(score)


