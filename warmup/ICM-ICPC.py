from itertools import combinations, izip

__author__ = 'julio'

n, m = raw_input().split()
n = int(n)
m = int(m)
people = (raw_input() for _ in xrange(n))
teams = combinations(people, 2)
topics = []
for (t1, t2) in teams:
    topics += [sum((1 for a, b in izip(t1, t2) if a == '1' or b == '1'))]
max_topics = max(topics)
print max_topics
print topics.count(max_topics)