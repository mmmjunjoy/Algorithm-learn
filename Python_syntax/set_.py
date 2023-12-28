

# set - 집합에 대한 연산

# 크게 3가지

# 1. 교집합
# 2. 합집합
# 3. 차집합


s1 = {1,2,3,4,5}

s2= {4,5,6,7}

#1. 교집합  - intersection()

print("교집합",s1.intersection(s2))

#2. 차집합

print("차집합",s1.difference(s2))

#3. 합집합

print("합집합",s1.union(s2))