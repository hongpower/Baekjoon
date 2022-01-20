# 분수
x = int(input())
diagN = 1 # 대각선으로 몇 개의 칸이 있는지 (1에서 1씩 증가)
cnt = 1 # 칸의 누적합
while True:
    if x <= cnt :
        leftover = cnt % x  # 나머지 (대각선 상에서 얼마나 움직일지 정하기 위해)
        if diagN % 2 == 0:
            numerator = diagN - leftover # 분자
            denominator = leftover+1 # 분모
            break
        else:
            numerator = leftover+1
            denominator = diagN -  leftover
            break
    else:
        diagN += 1
        cnt += diagN
print(f'{numerator}/{denominator}')

