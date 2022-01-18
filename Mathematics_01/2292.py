# 벌집
n = int(input())
beehouseN = 1 #벌집 수
cnt = 1 # 거쳐가는 집 개수

while True:
    if n <= beehouseN: # n이 이전 벌집수에서 현재 벌집수 사이에 있다면:
        print(cnt)
        break
    else:
        beehouseN += (6 * cnt)
        cnt += 1





