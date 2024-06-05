#백준 9095번


import sys

input = sys.stdin.readline


n = int(input())



# 점화식 - 항마다 관계가 있는 것.


# 미리 관계식을 이용하여, 키에 맞는 value 값을 계산한다.
a = {}

a[1] = 1
a[2] = 2
a[3] = 4

for i in range(4,11):
    a[i] = a[i-1] + a[i-2] + a[i-3]




for _ in range(n):
    x = int(input())
    print(a[x])









# 몫, 나머지로 접근 했었다.


# 총 6박스를 생성
# listbox = [[1], [1,2] ,[1,3] ,[2] ,[2,3] ,[3]]

#divmod -> 몫, 나머지

# for _ in range(n):
#     count = 0 

#     x = int(input())

#     for i in listbox:
#         print(i)
#         plus = 0 
#         for j in range(len(i)):
#             plus += i[j]
#         print("합", plus)
            
#         a ,b = divmod(x,plus)
#         if b == 0:
#             count += 1
        
#         else:

        



  
        


