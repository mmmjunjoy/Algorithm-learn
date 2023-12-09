

alluserlist = {'0': 'AA', '1': 'BB', '2': 'CC'}

# alluserlist - key,value 서로 변경 
Alluserlist = {v:k for k,v in alluserlist.items()}


# 해당 키의 value를 찾기 위한 - get
for i in Alluserlist.keys():
  print( Alluserlist.get(i))
