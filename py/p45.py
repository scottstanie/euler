def tri(limit):
    n = 1
    while n < limit:
        yield n * (n + 1) / 2
        n += 1


def pent(limit):
    n = 1
    while n < limit:
        yield n * (3 * n - 1) / 2
        n += 1


def hexag(limit):
    n = 1
    while n < limit:
        yield n * (2 * n - 1)
        n += 1


t = {n for n in tri(1000000)}
p = {n for n in pent(1000000)}
h = {n for n in hexag(1000000)}
print set.intersection(t, p, h)
