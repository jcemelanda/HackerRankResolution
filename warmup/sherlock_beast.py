__author__ = 'julio'
test_case = input()

for _ in xrange(test_case):

    digit_num = input()

    if not digit_num % 3:
        print '5' * digit_num
        continue

    fives = digit_num - 5

    while fives >= 3:

        if not fives % 3:
            print '5' * fives + '3' * (digit_num - fives)
            break
        else:
            fives -= 5
    else:
        if fives % 3 or fives < 0:
            print '-1'
            continue

        if not digit_num % 5:
            print '3' * digit_num