import sys



# 시간초과 문제로 인해

# list - search는  - O(n) 방식이다  . 
# 즉 , 처음부터 끝까지 다 탐색

# set - search는 - O(1) 방식이다.
# 바로 search완료

input = sys.stdin.readline

N = int(input())

alist = set(map(int,input().split()))

n = int(input())

blist = list(map(int,input().split()))



for i in range(n):
  if blist[i] in alist:
    print(1)
  else:
    print(0)