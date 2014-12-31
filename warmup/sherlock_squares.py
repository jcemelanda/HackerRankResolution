from __builtin__ import xrange
from math import sqrt

__author__ = 'julio'

test_cases = input()
for _ in xrange(test_cases):
    a, b = raw_input().split()
    a = int(a)
    b = int(b)+1
    #first square
    first_square = 0
    for i in xrange(a, b):
        if sqrt(i).is_integer():
            first_square = i
            break
    last_square = 0
    for i in xrange(b-1, a-1, -1):
        if sqrt(i).is_integer():
            last_square = i
            break
    if last_square == first_square == 0:
        print 0
    else:
        print int(sqrt(last_square)+1 - sqrt(first_square))