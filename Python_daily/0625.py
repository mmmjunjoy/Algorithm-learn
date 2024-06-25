# 백준 9375

import sys

input = sys.stdin.readline

test = int(input())

for _ in range(test):
    how = int(input())
    pracdict = {}
    count = 0
    for _ in range(how):
        a , b = input().split()
        if b not in pracdict.keys():
            pracdict[b] = []
            pracdict[b].append(a)
        
        else:
            pracdict[b].append(a)

    
    multi = 1
    for i in pracdict:
            multi= multi * (len(pracdict[i])+1)

    count += multi
    count -= 1
        

    

    print(count)



