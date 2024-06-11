#백준 - 1541번


import sys

input = sys.stdin.readline


# 최소를 만들기 위한 방법을 생각

# 그것은, -뒤에 괄호를 묶어서 최대한 크게 만들면 된다. 

# 즉, -와 -사이를 끊어주자


text = str(input())

mainlist = text.split("-")


result = 0

# 1. 처음부터 "-" 가 나올수 있다. 
if mainlist[0] == "":
    x = sum(map(int, mainlist[1].split("+")))
    print("1")
    result -= x
    for i in mainlist[2:]:
        y = sum(map(int, i.split("+")))
        result -= y


# 정상적으로 나올떄
else :
    x = sum(map(int, mainlist[0].split("+")))
    result += x

    for i in mainlist[1:]:
        y = sum(map(int, i.split("+")))
        result -= y


print(result)















# 숫자와 , 부호를 끊고 추후 방법이 도출 x

# text = str(input())


# numberlist = []
# plusminuslist = []

# a = ""
# for i in text:
#     if  i !=  "+" and i != "-":
#         a += i
#         print('a',a)

#     else :
#         numberlist.append(int(a))
#         a = ""
#         plusminuslist.append(i)
    
# numberlist.append(int(a))
    


    
# print("numberlist" , numberlist)

# print("plusminuslist" , plusminuslist)

