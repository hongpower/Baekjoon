# 더하기 사이클
countN = 0
n = int(input())
copyN = n

while True:
    first = n // 10
    second = n % 10
    middle = first + second
    n = (second * 10) + (middle % 10)
    countN += 1
    if n == copyN:
        break

print(countN)

