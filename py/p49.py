from p35 import is_prime
from collections import defaultdict
from itertools import chain, combinations

# eh i dont like this one

# 4 digit primes
primes = [p for p in range(1001, 10000, 2) if is_prime(p)]

# Make lists for the same sets of digits
digit_sets = defaultdict(list)
for p in primes:
    digit_sets[tuple(set(str(p)))].append(p)


for d_set, primes in digit_sets.iteritems():
    if len(primes) < 3:
        continue
    else:
        diff_counter = defaultdict(list)
        # Find the differences of all combos
        for a, b in combinations(primes, 2):
            diff = b - a
            diff_counter[diff].append((a, b))
        for diff, pair_list in diff_counter.iteritems():
            if len(pair_list) < 2:
                continue
            for idx, pair in enumerate(pair_list[:-1]):
                if pair[1] == pair_list[idx + 1][0]:
                    print pair_list
                    print ''.join(str(s) for s in set(chain.from_iterable(pair_list)))
