from p21 import proper_factors
import itertools


if __name__ == '__main__':
    upper_limit = 28123

    abundant = [i for i in range(1, upper_limit) if sum(proper_factors(i)) > i]
    abundant_sums = [sum(pair) for pair in itertools.product(abundant, repeat=2)]
    cant_be_abundant_sums = set(range(upper_limit)) - set(abundant_sums)

    print sum(cant_be_abundant_sums)
