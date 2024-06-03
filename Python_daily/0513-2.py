import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    a = "*" * (i+1)
    b = " "*(n-(i+1))
    print(b+a)

