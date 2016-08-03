import sys
import itertools

limit = int(sys.argv[1])


pents = {n * ((3 * n) - 1) / 2.0 for n in range(1, limit)}

diffs = ((i, j) for i, j in itertools.combinations(pents, 2) if abs(i - j) in pents)


def process_pents(tup):
    if sum(tup) in pents:
        print tup
        print abs(tup[0] - tup[1])
        return tup
    else:
        return


for t in diffs:
    process_pents(t)
