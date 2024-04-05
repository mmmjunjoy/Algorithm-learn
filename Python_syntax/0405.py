import sys

input = sys.stdin.readline


listprac = []
for _ in range(9):
    a = int(input())
    listprac.append(a)

maxnum = max(listprac)

indexresult = listprac.index(maxnum) + 1

print(maxnum)
print(indexresult)
