__author__ = 'julio'
test_cases = input()
for _ in xrange(test_cases):
    word = raw_input()
    l = len(word)/2
    operations = 0
    for i in xrange(l):
        operations += abs(ord(word[-(i+1)])-ord(word[i]))
    print operations