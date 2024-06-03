import sys

from itertools import permutations 

input = sys.stdin.readline

n , casino = map(int,input().split())

#list 안에 map으로 요소들 넣어주기
#map 아주 유용
listcard = list(map(int,input().split()))

resultlist = []
for three in permutations(listcard ,3):
    summix = sum(three)
    if summix > casino:
        continue
    else:
        resultlist.append(summix)
    

result = max(resultlist)

print(result)