
@api_view(['GET'])

def alluserAPI(request):

  url = 'https://api.channel.io/open/v4/user-chats?'

  headers = {'accept':'application/json' , 'x-access-key':'' , 'x-access-secret':''  }

  response = requests.get(url,headers=headers)

  print("응답" , response)

  
  items = response.json()

  # itmes['users] 에 mall들이 담긴다.
  # 이것을 for문 이용해서 추출해야된다 
  # res = items['users'][0]['profile']['mallId']  - > 여기서 [0] 인덱스 사용하여 추출

  alluser = items['users']

  alluserlen = len(items['users'])

  print("전체 user 길이",alluserlen)

  alluserlist = []

  ocnt = 0
  xcnt = 0
  nothavemalllist = []
  nothavemallid = []

  for i in range(len(items['users'])):
    print("hi")

    # profile에 mallId키가 존재한다면, 리스트에 포함

    # <!---key in dictionary 체크 문법 파트--->
    
    if 'mallId' in items['users'][i]['profile']:
      alluserlist.append( items['users'][i]['profile']['mallId'])
      ocnt += 1
    else:
      nothavemalllist.append( items['users'][i]['profile'])
      nothavemallid.append(i)
      xcnt += 1

    # <!---/key in dictionary 체크 문법 파트--->
  
  print("---------------------------------------------------------")
  
  print("mallid가지고 있는 업체 정보" , alluserlist)
  print("mallid 가지고 있는 업체 수" , ocnt)


  print("---------------------------------------------------------")

  print("mallid 안가지고 있는 업체 정보" , nothavemalllist)
  print("mallid 안가지고 있는 업체 수" , xcnt)
  print("mallid 안가지고 있는 업체 리스트" , nothavemallid)

  print("---------------------------------------------------------")


  items = items['users'][20]

  return Response(items)