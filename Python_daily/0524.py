import sys

input = sys.stdin.readline

N = int(input())


# 메모리 초과를 방지하기 위한 접근 방식

lst = [0] * 10001

for _ in range(N):
    dex = int(input())
    lst[dex] += 1


for i in range(len(lst)):
    while lst[i] > 0:
        print(i)
        lst[i] -= 1





# 메모리 초과가 걸린 코드

# praclist = []
# for i in range(N):
#     praclist.append(int(input()))

# # print("list",praclist)

# while len(praclist) > 0:
#     mins = min(praclist)
#     print(mins)
#     praclist.remove(mins)
    


