import sys

input = sys.stdin.readline

h,m = map(int, input().split())


if m < 45:
    help = m-45
    new = 60 + help
    if h == 0:
        h= 23
    else:
        h -= 1
    
else :
    new = m -45

print(h,new)
