__author__ = 'julio'
from collections import Counter
entry = raw_input()
if len(entry) % 2:
    ocurrencies = Counter(entry).values()
    odds = filter(lambda x: x % 2, ocurrencies)
    if len(odds) > 1:
        print 'NO'
    else:
        print 'YES'
else:
    ocurrencies = Counter(entry).values()
    odds = filter(lambda x: x % 2, ocurrencies)
    if odds:
        print 'NO'
    else:
        print 'YES'