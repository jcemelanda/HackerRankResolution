__author__ = 'julio'
test_cases = input()
for _ in xrange(test_cases):
    cuts = input()
    horizontal_cuts = cuts/2
    vertical_cuts = cuts - horizontal_cuts
    print horizontal_cuts * vertical_cuts
