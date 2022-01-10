# A+B-3
t = int(input())
lst = []
for i in range(t):
    a,b = map(int,input().split())
    lst.append(a + b)

for i in lst:
    print(i)
