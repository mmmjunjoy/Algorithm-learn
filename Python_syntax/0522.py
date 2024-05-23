import sys


input = sys.stdin.readline


n = int(input())

thatlist = list(map(int,input().split()))


maxins = max(thatlist)

resmulti = 0
for i in range(len(thatlist)):
    ins = float(thatlist[i]/maxins)*100
    # print(ins)
    resmulti += ins
    
    
res = resmulti/n

print(res)