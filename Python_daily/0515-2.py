import sys

input = sys.stdin.readline

box = int(input())

checking = 0
for i in range(1,box+1):
    multi = sum(map(int,str(i)))
    result = i + multi

    if result == box:
        checking +=1
        print(i)
        break
    
    
if checking == 0:
    print("0")
