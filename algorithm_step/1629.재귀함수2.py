#첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.



# 시간초과가 걸린다

import sys

input = sys.stdin.readline

sys.setrecursionlimit(10000)

a , b , c = map(int, input().split())

def multi(result,A,n):

  cnt = 0
  
  result = result *A


  if cnt == n-1:
  
    result = result % c
    print(result)

    return
  
  cnt += 1


  multi(result,A ,n-1)


multi(1,a,b)
  
  
