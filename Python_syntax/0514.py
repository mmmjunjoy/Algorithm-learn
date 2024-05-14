import sys

input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

multi = str(a*b*c)

print(multi)

# count 이용

# for i in range(10):
#     print(multi.count(str(i)))


# dict 이용 

dicts = {}
for i in range(10):
    dicts[i] = 0

for j in multi:
    dicts[int(j)] +=1

for i in dicts:

    print(dicts.get(i))
  

print(dicts)