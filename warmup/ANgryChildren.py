__author__ = 'julio'
entries = input()
packets = input()
options = [int(input()) for _ in xrange(entries)]
options.sort()
unfairness = 1e9
for i in xrange(entries-packets):
    _unfairness = options[i+packets-1] - options[i]
    if _unfairness < unfairness:
        unfairness = _unfairness
print unfairness