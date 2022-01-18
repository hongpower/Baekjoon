# 손익분기점
import sys

a, b, c = map(int,sys.stdin.readline().split())
if b >= c :
    print(-1)
else:
    n = int(a/(c-b))
    print(n + 1)

