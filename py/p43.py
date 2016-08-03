import itertools


def div_check(n):
    primes = [2, 3, 5, 7, 11, 13, 17]
    return all(s % primes[idx] == 0 for idx, s in enumerate(slices(n)))


def slices(n):
    for idx in range(1, 8):
        yield int(n[idx: idx + 3])

total = 0
for n in itertools.permutations('0123456789'):
    n = ''.join(n)
    if div_check(n):
        print n
        total += int(n)


print total
