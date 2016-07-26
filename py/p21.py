from p12 import factors


def proper_factors(n):
    return factors(n) - {n}


def d(n):
    '''Remove the number from factors to make proper factors, then sum'''
    return sum(factors(n) - {n})


if __name__ == '__main__':
    ds = {i: d(i) for i in range(1, 10000)}

    amicable = set()
    for i in range(1, 10000):
        if i == ds.get(ds[i]) and i != ds[i]:
            amicable.add(i)

    print amicable
    print sum(amicable)
