import sys

input = sys.stdin.readline

n = int(input())


#list에 한번에 담기
praclist = list(map(int, input().split()))


#오름차순으로 정렬
praclist.sort()

result = 0

for i in range(n):

    newn = n -i
    result += praclist[i] * newn
  

print(result)

