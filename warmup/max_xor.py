__author__ = 'julio'
from itertools import combinations_with_replacement
L = input()
R = input()

combinations = combinations_with_replacement(xrange(L, R+1), 2)
xor = (x^y for x, y in combinations)
print max(xor)
