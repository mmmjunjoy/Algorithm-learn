# 서로 다른 N개의 자연수의 합이 S라고 한다. 
# S를 알 때, 자연수 N의 최댓값은 얼마일까?

# 입력
# 첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

# 출력
# 첫째 줄에 자연수 N의 최댓값을 출력한다.


# while사용 , 수식 정리

import sys

input = sys.stdin.readline

ns = int(input())



n = 1

while True:
  if n*n + n > 2* ns :
    break
  else:
    n += 1


n -= 1

print(n)