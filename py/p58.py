import numpy as np
from p28 import count_diags


def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) / (2 * i) + 1)
    return [2] + [i for i in xrange(3, n, 2) if sieve[i]]


def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False

last_prime = 100000000
primes = set(primesfrom2to(1000000000))
print 'Found primes'

side_len = 100000
diag_generator = count_diags(side_len)
diag_generator.next()
diag_generator.next()

diags = {1, 3, 5, 7}
total_diags = 2
prime_diags = 1
while float(prime_diags) / float(total_diags) > 0.10:
    try:
        d = diag_generator.next()
    except:
        break
    if d in primes:
        prime_diags += 1
    total_diags += 1
    if total_diags % 10000 == 0:
        print total_diags
        print prime_diags

print 'Total diags:', total_diags
print 'Primes: ', prime_diags
print 'Side length: ', total_diags / 2 + 1
