# 단어 공부
## 딕셔너리에서 for i in dict 하면 i는 키가 나온다!!
## .upper() -> 데이터만
## 딕셔너리의 max하면 키의 max출력

user_input = list(i for i in input()) # 받은 값

alphaupper = list(map(lambda x: x.upper(), user_input)) # 입력값을 모두 대문자로 만들어서 문자 하나씩 리스트에 추가
alphaSingle = set(alphaupper) # 중복 알파벳문자는 제외한 세트.

alphas = []
nums = []

for a in alphaSingle: # 알파벳 문자 하나씩 a로 받아옴
    cntN = alphaupper.count(a) # 알파벳 문자가 몇개 있는지 개수
    nums.append(cntN) # nums리스트에는 알파벳 개수를 입력
    alphas.append(a) # alphas리스트에는 해당 알파벳을 입력

maxN = max(nums) # nums리스트에 있는 알파벳개수 숫자 중 가장 큰 값
if nums.count(maxN) > 1: # max숫자가 여러개라면
    print('?') # ?출력
else:
    print(alphas[nums.index(maxN)]) #nums의 max숫자의 인덱스를 이용해서 alphas에서 단어 출력 (문자와 숫자는 같은 인덱스에 위치 하므로)
