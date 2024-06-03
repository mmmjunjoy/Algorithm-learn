import sys


input = sys.stdin.readline


a ,n = map(int,input().split())


prac = 0
mini = 1
for i in range(1,a+1):
    prac += 1

    if prac <= n:
        mini = mini * i
  


prac2= 0
max = 1
for j in reversed(range(1,a+1)):
    prac2 += 1

    if prac2 <= n:
        max = max * j

    

result = int(max / mini)

print(result)





