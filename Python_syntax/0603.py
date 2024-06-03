import sys

input = sys.stdin.readline

n,k = map(int,input().split())


reallist = []
for i in range(n):
    a = int(input())
    reallist.append(a)


# 새로운 풀이 - 나머지, 몫 이용

# lists.sort(reverse=True)

# count = 0
# for j in lists:
#     if k >= j:
#         count += (k // j)
#         k = k % j

#         if k <= 0:
#             break

# print(count)



# 왜 틀린것인가.


# for j in lists:
#     if j <= k:
#         reallist.append(j)




count = 0
prac = 0

while True:
        prac += reallist[-1]
        if prac < k:
            count += 1

        elif prac > k:
            prac -= reallist[-1]
            reallist.remove(reallist[-1])
        
        else:
            count +=1
            break


    
print(count)



