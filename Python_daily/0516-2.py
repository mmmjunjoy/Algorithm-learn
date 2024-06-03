from itertools import permutations


pool = ['a','b','c']

threemix = list(map(''.join,permutations(pool)))

twomix = list(map(''.join,permutations(pool,2)))


print("threemix" ,threemix)

print("twomix",twomix)