# # 그룹 단어 체커
# # 1) 다른 사람 참고:
# n = int(input())
# cnt = n
# for _ in range(n):
#     word = input()
#     for w in range(len(word)-1):
#         if word[w] == word[w+1]:
#             pass
#         elif word[w] in word[w+1:]: # 알파벳이 존재하는데 바로 다음에가 아니라면
#             cnt -=1
#             break
# print(cnt)
#
# # 2) enumerate활용 by me
# n = int(input())
# cnt = n
#
# for _ in range(n):
#     lst = []
#     word = input()
#     for indexL, letter in enumerate(word):
#         if letter not in lst:
#             lst.append(letter)
#         else:
#             if letter == lst[indexL-1]:
#                 lst.append(letter)
#                 pass
#             else:
#                 cnt -=1
#                 break
# print(cnt)

N=int(input())
for i in range(N):
    a=input()
    if list(a)!=sorted(a,key=a.find):
        N-=1
print(N)

