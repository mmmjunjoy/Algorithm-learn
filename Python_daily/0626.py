import sys

input = sys.stdin.readline


N ,M = map(int,input().split())


# 누적합을 이용
nlist = [0]
nlist += list(map(int,input().split()))


# 누적합 배열을 생성하기 위해 :  enumerate -> index , 해당값
for i , num in enumerate(nlist):
    if i>0:
        nlist[i] = nlist[i-1] + num


for _ in range(M):
    a ,b = map(int,input().split())
    result = nlist[b] - nlist[a-1]
    print(result)




# 시간초과 -> 인덱스와 인덱스사이의 값을 각각 추출하여 더해주는 방식이라

# nlist = []
# nlist.append(input().split())


# for _ in range(M):
#     a,b = map(int,input().split())
#     a -= 1
#     count = 0
#     for i in range(a,b):
#         count += int(nlist[0][i])
    
#     print(count)

# print("nlist",nlist)
