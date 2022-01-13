# 평균
n = int(input())
grade = list(map(int,input().split())) 
maxG = max(grade)
newgrade = 0
for i in range(n):
     newgrade += grade[i] / maxG * 100
print(newgrade/n)