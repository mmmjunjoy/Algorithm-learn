
import sys


input = sys.stdin.readline

zum , line = map(int,input().split())

# max 연결요소 갯수
max = zum //2 

dicts ={}
for i in range(1,zum+1):
    dicts[i] = []


for _ in range(line):
    a , b = map(int, input().split())

    if b not in dicts[a]:
        dicts[a].append(b)
    


for i in range(1,zum+1):
    for j in dicts[i]:
        if dicts[j] != []:
            for k in dicts[j]:
                dicts[i].append(k)
           

print("dicts",dicts)



print(max)
print(zum)
print(line)