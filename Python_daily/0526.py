import sys


input = sys.stdin.readline


N = int(input())

mainpoint = 666
count = 0

while True:
    if '666' in str(mainpoint):
        count += 1

        if count == N:
            break

    mainpoint +=1


print(mainpoint)

