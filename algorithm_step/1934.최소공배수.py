import sys

input = sys.stdin.readline


n = int(input())

for i in range(n):
    a ,b = map(int,input().split())
    
    alist = []
    blist = []
    for i in range(1,a+1):
        if a % i == 0:
            alist.append(i)
    # print("alist",alist)
        
    for j in range(1,b+1):
        if b % j == 0:
            blist.append(j)
    # print("blist", blist)

    res = []
    for g in range(len(alist)):
        if alist[g] in blist:
            res.append(alist[g])
    
    # print("res",res)
    
    max = 1
    for r in range(len(res)):
        max *= res[r]
    
    # print("max",max)

    amax = a // max

    if amax == 0:
        amax = 1

    # print("amax", amax)


    bmax = b // max
    if bmax == 0:
        bmax = 1
    # print("bmax", bmax)

    result = max * amax * bmax

    print(result )

    
        

