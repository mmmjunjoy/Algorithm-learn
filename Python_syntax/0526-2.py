import sys

input = sys.stdin.readline


N = int(input())



mainlist = []

for i in range(N):
    age ,name = map(str,input().split())
    mainlist.append((int(age),name,i))

mainlist.sort(key = lambda x : (x[0],x[2]))

for i in mainlist:
    print(i[0],i[1])


# 입력 순서를 고려하지 못한다?

# dicts ={}

# for i in range(N):
#     age , name = map(str,input().split())
#     dicts[name] = int(age)

# d2 = sorted(dicts.items(), key=lambda x: x[1])


# for key, value in d2:
#     print(value, key)




