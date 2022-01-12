# 나머지
# lst = []
# cnt = 0
# for i in range(10):
#     lst.append(int(input())%42)
# for i in lst:
#     if i not in lst2:
#         cnt += 1
#         lst2.append(i)
# print(cnt)

# 다른 사람꺼 참고해서 새로 생성:
# set 특성 사용
lst = []
for i in range(10):
	lst.append(int(input())%42)
print(len(set(lst)))

