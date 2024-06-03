import sys

input = sys.stdin.readline

n , m = map(int, input().split())


dicts  = {}
for i in range(n):
    domain , password = input().split()

    dicts[domain] = password





resultlist = []
for j in range(m):

    # strip 이 중요하다 -> '/n' 까지 포함 되어서 key값에 없다고 나오기 때문이다.
    finddomain = str(input().strip())

    result = dicts[finddomain]

    print(result)
    


