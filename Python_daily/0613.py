# 백준 11723

import sys

input = sys.stdin.readline


# set과 dict 의 차이
mainlist = {"."}

# discard와 remove 차이

n = int(input())

for _ in range(n):

    a = input().strip()
    # print(a)
    if a == "all":
        # print("hi")
        mainlist ={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
        continue

    elif a =="empty":
        mainlist = {"."}
        continue
    

    else:
        x,y = a.split(" ")

        # print("xy")

        if x == "add":
            mainlist.add(int(y))
            
        elif x =="remove":

            mainlist.discard(int(y))
            
        elif x =="check":
            if int(y) in mainlist:
                print("1")
                
            else:
                print("0")
            
        elif x =="toggle":
            if int(y) in mainlist:
                mainlist.discard(int(y))
            else:
                mainlist.add(int(y))

        # print(mainlist)

# print("mainlist" , mainlist)


# add 1
# add 2
# check 1
# check 2
# check 3
# remove 2
# check 1
# check 2
# toggle 3
# check 1
# check 2
# check 3
# check 4
# all
# check 10
# check 20
# toggle 10
# remove 20
# check 10
# check 20
# empty
# check 1
# toggle 1
# check 1
# toggle 1
# check 1


# 1  
# 1
# 0
# 1
# 0
# 1
# 0
# 1
# 0
# 1
# 1
# 0
# 0
# 0
# 1
# 0



# 1
# 1
# 0
# 1
# 0
# 1
# 0
# 1
# 0
# 1
# 1
# 0
# 0
# 0
# 1
# 0