import sys


input = sys.stdin.readline

N = int(input())

plus = 1

for i in range(1,N+1):
    plus *= i


strs = str(plus)


result = 0
for i in range(len(strs)):

    dex = len(strs) - (i+1)
    # print(strs[dex])

    if strs[dex] != '0':
        print(result)
        break
    
    if strs[dex] == '0':
  
        result += 1
    
    
    