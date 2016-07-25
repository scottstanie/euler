# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
from collections import Counter


def number_to_counter(n):
    '''Convert to structure counting instances of digits'''
    return Counter(str(n))


def same_digits(m, n):
    return number_to_counter(m) == number_to_counter(n)


def get_multiples(n):
    return (idx * n for idx in range(3, 7))

if __name__ == '__main__':
    idx = 1
    found_number = False

    while not found_number:
        idx += 1
        check = 2 * idx
        found_number = all(same_digits(check, num) for num in get_multiples(idx))

    print "Number: %s" % idx
    print "Multiples:"
    print [check] + list(get_multiples(idx))
