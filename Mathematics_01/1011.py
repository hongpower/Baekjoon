# Fly me to the Alpha Centauri
import sys

t = int(sys.stdin.readline())
for i in range(t):
    x, y = map(int,(sys.stdin.readline().split()))
    dis = y - x
    cnt = 0

    moveDis = 1
    total_move = 0

    while total_move < dis:
        cnt += 1
        total_move += moveDis
        if cnt % 2 == 0:
            moveDis +=1

    print(cnt)




