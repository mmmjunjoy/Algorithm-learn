# 17626 백준


import sys

input = sys.stdin.readline


puts = int(input())


# 재귀함수 사용 , 하나하나 다 해보아서, 만족하는 것을 찾는 방법

def bing(x,y):
    count = y
    if x <= 0:
        return 0 

    elif x >0:

        for i in range(1, x+1):
            print("x",x)
            start = i
            point = i*i
            if x == point:
                count += 1
                print("lastpoint", point)
                print("last",x)
                print("count",count)
                return count
            
            elif x < point:
                count += 1
                start = i-1
                x -= start*start
      
                return bing(x,count)            
            

bing(puts,0)

