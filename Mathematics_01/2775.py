## 부녀회장이 될테야
# k : 층 n: 호
# 0층부터 1호까지. 0층의 i호에는 i명이 산다
# 1)
# import sys
# t = int(sys.stdin.readline())
#
# # 한 층 거주자 (Resident Num)
# for repeat in range(t):
#     k = int(sys.stdin.readline())  # 층수
#     n = int(sys.stdin.readline())  # 호수
#     ResN = [i for i in range(1,n+1)]
#     floor = 0
#
#     while True:
#         floor += 1
#         for j in range(1,n):
#             ResN[j] = ResN[j-1] + ResN[j]
#         if floor == k:
#             break
#
#     print(ResN[n-1])


# 2) 누적함수
t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    res_floor = [i for i in range(1, n+1)]
    print(res_floor)
    for _ in range(k): ## 층수만큼 반복
        for i in range(1, n): ## 호수만큼 반복
            res_floor[i] += res_floor[i-1]
            # print(res_floor)
        print(res_floor)
    print(res_floor[-1])






