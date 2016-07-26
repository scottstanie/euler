from math import sqrt
from decimal import Decimal


def fib(n):
    '''Nth fibonacci number'''
    return int((((1 + Decimal(sqrt(5)))**n) - (1 - Decimal(sqrt(5)))**n) / (2**n * Decimal(sqrt(5))))

if __name__ == '__main__':
    for i in range(200, 10000):
        if len(str(fib(i))) >= 1000:
            print i
            break
    print i, fib(i), len(str(fib(i)))
