# 이 문제는 아주 평범한 배낭에 관한 문제이다.

# 한 달 후면 국가의 부름을 받게 되는 준서는 여행을 가려고 한다. 세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에, 가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.

# 준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.



# 첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.

# 입력으로 주어지는 모든 수는 정수이다.


# 4 7
# 6 13
# 4 8
# 3 6
# 5 12


import sys


input = sys.stdin.readline


kind , weight = map(int,input().split())


wlist = []
vlist = []

for i in range(kind):
  w,v = map(int,input().split())
  wlist.append(w)
  vlist.append(v)


falselist = [False] * kind




# 1. 무게가 아래로 셋팅이 되는 조합 수를 구하자

resw = 0
resv = 0

reswlist = []
resvlist = []

def vv(n,resw,resv):


  if falselist[-1] == True:
    return
  

  falselist[n] = True

  # print("현재 falselist", falselist)

  # print("현재의 n", n)

  
  for i in range(n, kind):
      

      resw += wlist[i]
      resv += vlist[i]
      if resw > weight:
        resw -= wlist[i]
        # print("resw", resw)
        resv -= vlist[i]
        continue
      reswlist.append(resw)
      resvlist.append(resv)

  vv (n+1 ,0 ,0 )


vv(0, resw ,resv)

# print("reswlist", reswlist)
# print("resvlist", resvlist)


print( max(resvlist))

# 2. 각 조합에 해당되는 물건들 v의 합을 구하자




