__author__ = 'julio'

test_cases = input()
for i in xrange(test_cases):
    cycles = input()
    height = 1
    for cycle in xrange(1, cycles+1):
        if cycle % 2:
            height *= 2
        else:
            height += 1
    print height