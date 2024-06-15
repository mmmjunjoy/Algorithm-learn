#11724

#dfs
import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline

N , M = map(int, input().split())


graph = list([] for _ in range(N+1))

for _ in range(M):
    u , v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)


visted = [False]*(N+1)


def DFS(x):
    visted[x] = True

    for node in graph[x]:
        if not visted[node]:
            DFS(node)
cnt = 0
for i in range(1,N+1):
    if not visted[i]:
        DFS(i)
        cnt += 1



# print('graph' , graph)
# print('visited',visted)
print( cnt)



# dicts ={}
# for i in range(1,N+1):
#     dicts[i] = []


# for _ in range(M):
#     u ,v = map(int,input().split())
#     dicts[u].append(v)

# print("dicts",dicts)