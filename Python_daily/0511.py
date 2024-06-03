

import sys

input = sys.stdin.readline

n = int(input())

realnumber = int(input())



box = []


for i in str(realnumber):
    box.append(i)


print('testbox',box)

result = 0
for i in box:
    a = int(i)
    result +=a


print("result", result)
