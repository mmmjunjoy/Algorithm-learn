import sys

input = sys.stdin.readline

btn = True



while(btn):
    res = 0
    a = int(input())
    if a == 0:
        btn = False
        break
    a2 = len(str(a))//2

    if len(str(a)) == 1:
        print("yes")

    for i in range(len(str(a))):
        origin = str(a)[i]
        i = len(str(a)) - i
        used = str(a)[i-1:i]
        if origin != used:
            print("no")
            break
            
        else:
            res+=1
            
        if res == a2:
            print("yes")

       
                