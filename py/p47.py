import itertools
from p35 import is_prime
from p549 import prime_factorize


cur_streak = 0
start = 1

# for n in range(1001, 10000):
for n in range(99999, 1000000):
    cur_streak += 1
    factors = set(prime_factorize(n))
    if len(factors) != 4:
        cur_streak = 0
        start = n + 1
        continue
    else:
        if cur_streak >= 4:
            print 'break'
            break

print start
print [set(prime_factorize(n)) for n in range(start, start + 4)]
