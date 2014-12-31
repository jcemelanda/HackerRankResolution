__author__ = 'julio'


test_cases = input()

for i in xrange(test_cases):
    num = input()

    ant = 0
    x = 1
    count = 0
    while True:
        count += 1
        if count == 1:
            ant = x
        else:
            ant, x = x, x+ant
        if x > num:
            break

    if num == ant:
        print "IsFibo"
    else:
        print "IsNotFibo"
