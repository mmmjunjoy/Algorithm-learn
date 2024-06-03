
#dfs와 bfs구현을 위한 dict 제작

import sys

input = sys.stdin.readline

n,m,v = map(int,input().split())


dict = {i:[] for i in range(1,n+1)}

print("Dict", dict)

for i in range(m):

    # dict 도 int로 변환이 되야 key에 접근이 가능하다
    a,b = map(int,input().split())
    dict[a].append(b)
    dict[b].append(a)

print("dict2", dict)

