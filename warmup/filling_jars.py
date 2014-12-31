__author__ = 'julio'
n, m = raw_input().split()
n = int(n)
m = int(m)

jars = 0
for _ in xrange(m):
    a, b, k = raw_input().split()
    a = int(a) - 1
    b = int(b)
    k = int(k)
    jars += k*(b-a)

print jars / n