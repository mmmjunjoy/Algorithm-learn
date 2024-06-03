import sys

input = sys.stdin.readline

num = int(input())

for i in range(num):

    # 오른쪽 개행문자를 제거해주는 것이 중요하다.
    q = input().rstrip()

    n = int(q[0])

    s = q[1:]
    s = s.replace(" ","")

    result = ""
    for j in range(len(s)):
        result += s[j]*n

    result = result.replace(" ","")
    # print(n)
    # print(s)
    print(result)