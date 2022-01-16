# 상수
num1, num2 = input().split()

numback1 = int(num1[2]+num1[1]+num1[0])
numback2 = int(num2[2]+num2[1]+num2[0])

if numback1 > numback2 :
    print(numback1)
else:
    print(numback2)