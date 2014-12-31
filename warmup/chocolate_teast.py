t = int(raw_input())
for i in xrange(t):
    input_string = raw_input()
    n, c, m = [int(x) for x in input_string.split()]

    chocolates = n/c
    packs = chocolates
    total_chocolates = chocolates
    while packs/m:
        extra_chocolate = packs / m
        packs = packs % m
        packs += extra_chocolate
        total_chocolates += extra_chocolate
    print total_chocolates
