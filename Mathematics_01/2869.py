import sys
# # 달팽이는 올라가고 싶다
# a, b, v = map(int,input().split())
# dis = v-a # 낮에 갈 수 있는 거리를 한번 뺀 달팽이야 가야할 거리
# oneday = a - b # 하루동안 갈 수 있는 거리
# days = dis//oneday # 하루거리량으로 dis거리는 얼마나 갈 수 있는지
# if dis%oneday == 0: # 만약 나머지가 없다면 달팽이는 밤이 되기 전에 하루만 더주면 갈 수 있다
#     print(days + 1)
# else:
#     print(days + 2) # 만약 나머지가 있다면 달팽이는 낮에 가지 못한다

# 다른 사람 코드
A, B, V = map(int,sys.stdin.readline().split())
day = (V - B) / (A - B)
print(day)
print(int(day) if day == int(day) else int(day) + 1) # 굳이 나머지를 이용하지 않고, 소수인 day를 int로바꿨을때 같은 값인지 아닌지 보고 판단.

# math.ceil()/math.floor() => 내림기능/올림기능