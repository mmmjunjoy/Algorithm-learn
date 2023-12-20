
#루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input())


dict = {i:[] for i in range(1,N+1)}

print("key", dict.keys())

for i in range(1,N):
  R,T = map(int,input().split())
  if R in dict.keys():
    dict[R].append(T)


def Tree(V):
  


print("dict" , dict)