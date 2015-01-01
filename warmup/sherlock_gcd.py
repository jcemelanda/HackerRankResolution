__author__ = 'julio'

from itertools import combinations
import fractions

def gcd(L):
    return reduce(fractions.gcd, L)

test_cases = input()

for _ in xrange(test_cases):
    number_count = input()
    numbers = set([int(x) for x in raw_input().split()])
    number_count = len(numbers)
    divison_in_set = False
    for i in xrange(number_count, 1, -1):
        options = combinations(numbers, i)
        for option in options:
            if gcd(option) == 1:
                break
        else:
            if i == number_count:
                divison_in_set = True
                break
            continue
        break
    else:
        print 'NO'
        continue
    if divison_in_set:
        print 'NO'
        continue
    print 'YES'