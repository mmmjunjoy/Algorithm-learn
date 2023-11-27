# 태수가 즐겨하는 디제이맥스 게임은 각각의 노래마다 랭킹 리스트가 있다. 이것은 매번 게임할 때 마다 얻는 점수가 비오름차순으로 저장되어 있는 것이다.

# 이 랭킹 리스트의 등수는 보통 위에서부터 몇 번째 있는 점수인지로 결정한다. 하지만, 같은 점수가 있을 때는 그러한 점수의 등수 중에 가장 작은 등수가 된다.

# 예를 들어 랭킹 리스트가 100, 90, 90, 80일 때 각각의 등수는 1, 2, 2, 4등이 된다

# 랭킹 리스트에 올라 갈 수 있는 점수의 개수 P가 주어진다. 그리고 리스트에 있는 점수 N개가 비오름차순으로 주어지고, 태수의 새로운 점수가 주어진다. 이때, 태수의 새로운 점수가 랭킹 리스트에서 몇 등 하는지 구하는 프로그램을 작성하시오. 만약 점수가 랭킹 리스트에 올라갈 수 없을 정도로 낮다면 -1을 출력한다.

# 만약, 랭킹 리스트가 꽉 차있을 때, 새 점수가 이전 점수보다 더 좋을 때만 점수가 바뀐다.

# 3 90 10
# n /새로운 점수/p 

# 100 90 80


# a.index()  -> index값이 도출되는 것
# list[-1]  -> 마지막 요소 도출


import sys
input = sys.stdin.readline

a = list(map(int,input().split()))
blist = list(map(int,input().split()))


newscore = a[1]
limits = a[2]

if newscore in blist:
  twin  = blist.index(newscore)+1
  if twin >= limits:
    print("-1")
  else:
    print(twin)

else:
  blist.append(newscore)
  blist = sorted(blist , reverse=True)    
  res = blist.index(newscore) + 1
  if res > limits :
    print("-1")
  else:
    print(res)




