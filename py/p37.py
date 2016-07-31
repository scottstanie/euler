from p35 import is_prime


def trunc(p):
    length = len(str(p))
    for idx in range(length):
        test1 = int(str(p)[idx:])
        test2 = int(str(p)[:length - idx])

        # print test1, test2
        if not is_prime(test1) or not is_prime(test2):
            return False

    return True


p = 23
trunc_primes = []
while len(trunc_primes) < 11:
    if is_prime(p) and trunc(p):
        trunc_primes.append(p)
    p += 2
print trunc_primes
print sum(trunc_primes)
