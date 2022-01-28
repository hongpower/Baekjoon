# 설탕 배달
n = int(input())
bagsN = 0

while True:
    if n % 5 == 0 : # 5의 배수라면 바로 반복문 stop
        bagsN += n // 5
        print(bagsN)
        break
    n -= 3
    bagsN += 1
    if n <= 3:
        if n % 3 == 0: # 0과 3의 경우.
            bagsN += n // 3 # 0 나누면 0 반환
            print(bagsN)
            break
        else:
            print(-1)
            break

