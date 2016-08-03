from p35 import is_prime
from collections import defaultdict
from itertools import combinations

# eh i dont like this one

# 4 digit primes
primes = [p for p in range(1001, 10000, 2) if is_prime(p)]

digit_sets = defaultdict(list)
for p in primes:
    digit_sets[tuple(set(str(p)))].append(p)


# digit_sets = {tuple(set(str(3449))): [3449, 3499, 3943, 4339, 4349, 4493, 4933, 4943, 4993, 9343, 9349, 9433, 9439]}

for d_set, primes in digit_sets.iteritems():
    if len(primes) < 3:
        continue
    else:
        diff_counter = defaultdict(list)
        for a, b in combinations(primes, 2):
            # print '-----'
            diff = b - a
            if a == 1487 and b == 4817:
                print a, b, diff
            # print a, b, diff
            diff_counter[diff].append((a, b))
            # found = False
        #     cur = b + diff
        #     if cur in primes:
        #         cur += diff
        #         count += 1
        #         if count >= 3:
        #             print a, b, diff, cur
        #             break
        # print diff_counter.most_common()
        if 3330 in diff_counter:
            print diff_counter
            print '===='*8
        if any(len(diff_list) >= 2 for diff_list in diff_counter.values()):
            # print diff_counter
            print [(diff, prime_list) for diff, prime_list in diff_counter.iteritems() if len(prime_list) >= 2]
                # print [i - j for i, j in zip(prime_list[:-1], prime_list[1:])]
            print
            print primes
            print '\n'

    # elif len(primes) == 3:
    #     diffs = [i - j for i, j in zip(primes[:-1], primes[1:])]
    #     if len(set(diffs)) == 1:
    #         print primes
