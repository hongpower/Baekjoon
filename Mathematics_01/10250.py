## ACM 호텔
import sys
t = int(input())
for i in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    roomN, floorN = divmod(n,h)
    if floorN == 0: # 나머지가 0일 때는 맨 꼭대기 층 배정되도록 예외 설정
        roomN -=1
        floorN = h

    if roomN < 9:
        print(f'{floorN}0{roomN+1}')
    else:
        print(f'{floorN}{roomN+1}')

