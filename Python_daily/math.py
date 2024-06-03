# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.


# 시간초과가 나온다  // 테스트케이스는 통과

import sys

input = sys.stdin.readline

num = int(input())

cnt = 0

while  num != 1:

  if num % 3 == 0:
    num = num / 3
    cnt += 1 
    if num == 1:
      break
  else : 
    num = num -1 
    cnt += 1
    if num == 1:
      break
    if num % 3 == 0:
      num  = num / 3
      cnt += 1
      if num == 1:
        break
    else :
      num = num / 2
      cnt += 1
      if num == 1:
        break

print(cnt)


# 답 

# dp문제라고 한다.
# 규칙을 찾고 , 최솟값을 구하기 위해 값을 저장시켜놓고 사용한다

x = int(input())

d = [0] * (x+1)

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    
print(d[x])