import sys

input = sys.stdin.readline

# 백트래킹 문제

#  아래 코드는 m이 2일때만 가능,
#  m 이 2이상으로 커질경우 불가능,,

N,M = map(int,input().split())

parent = []

# 최종적 매치 위한 parent list 생성
for i in range(1,N+1):
    parent.append(i)

print("parent",parent)

for i in range(1,N+1):
    res = []
    baby = []
    for j in range(1,N+1):
    
        # 최종적으로 매칭시키기 위한 babylist 만들기
        if j is not i:
            baby.append(j)
        
    print("baby" ,baby)
        

    lenres =M 

   
    for b in baby:
        res.append(i)
        if i in res:
            res.append(b)

            if len(res) == lenres :
                print("res",res)
                res.clear()
    

             
                


        
        
    


    
    




