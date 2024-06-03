import sys


input = sys.stdin.readline




while True:
    praclist = []
    a,b,c = map(int,input().split())

    if a == b == c == 0 :
        break
    praclist.append(a)
    praclist.append(b)
    praclist.append(c)

    maxs = max(praclist)

    praclist.remove(maxs)

    if maxs*maxs == praclist[0]*praclist[0] +praclist[1]*praclist[1]:
        print("right")

    else:
        print("wrong")



