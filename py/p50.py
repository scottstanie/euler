from p35 import is_prime


def next_prime(p):
    if not is_prime(p):
        return
    while True:
        p += 2
        if is_prime(p):
            yield p

primes = [2] + [p for p in range(3, 1000000, 2) if is_prime(p)]
print primes[:10]
prime_set = set(primes)

max_len = 0

for idx in range(len(primes)):
    for slice_len in range(449, 550):
        prime_sum = sum(primes[idx: idx + slice_len])
        if prime_sum in prime_set and slice_len > max_len:
            max_len = slice_len
            print prime_sum, slice_len
