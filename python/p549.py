import sys
from p35 import is_prime
from collections import Counter

already_factored = {}
prime_numbers = set()
found_min_factorial = {}


def factorize(n):
    if n in already_factored:
        return already_factored[n]
    if is_prime(n):
        return [n]

    d = 2
    factors = []
    count = 0
    while n > 1:
        count += 1
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1
        if n in already_factored:
            factors.extend(already_factored[n])
            break

    already_factored[n] = factors
    return factors


def find_min_factorial(n):
    if n in prime_numbers or is_prime(n):
        prime_numbers.add(n)
        return n
    else:
        if n in found_min_factorial:
            return found_min_factorial[n]

        if n in already_factored:
            factors = already_factored[n]
        else:
            factors = factorize(n)
            already_factored[n] = factors

        if n % 100 == 0:
            print 'n is 100', n
            # print found_min_factorial
        factors_needed = Counter(factors)
        min_factorial = 1
        current_factors = Counter()
        while factors_needed - current_factors:
            min_factorial += 1
                # print 'min_factorial: ', min_factorial
                # print 'factors needed:', factors_needed
                # print 'current factors: ', current_factors
            new_factors = factorize(min_factorial)
            current_factors += Counter(new_factors)

        found_min_factorial[n] = min_factorial
        return min_factorial


def S(n):
    return sum(find_min_factorial(n) for n in range(2, n + 1))


if __name__ == '__main__':
    try:
        input_num = int(sys.argv[1])
    except:
        print "Usage: python p549.py <int>"
        sys.exit(1)

    f = factorize(input_num)
    print f

    print find_min_factorial(input_num)

    for i in range(100000):
        factorize(i)
    # print S(input_num)
