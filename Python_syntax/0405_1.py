


import sys

input = sys.stdin.readline

years = int(input())

if years % 4 != 0:
    print(0)

else:
    if years % 100 == 0:
        if years % 400 == 0:
            print(1)
        else:
            print(0)
    else:
        print(1)

