from p12 import factors


def d(n):
    '''Remove the number from factors to make proper factors, then sum'''
    return sum(factors(n) - {n})


ds = {i: d(i) for i in range(1, 10000)}

amicable = set()
for i in range(1, 10000):
    if i == ds.get(ds[i]) and i != ds[i]:
        amicable.add(i)

print amicable
print sum(amicable)
