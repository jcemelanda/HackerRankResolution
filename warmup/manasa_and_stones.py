__author__ = 'julio'
test_cases = input()
for _ in xrange(test_cases):
    stones = input()
    v1 = input()
    v2 = input()
    options = set()
    for i in xrange(stones):
        options.add(i*v1+(stones-1-i)*v2)
    options = [str(x) for x in sorted(list(options))]
    print ' '.join(options)