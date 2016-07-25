import math


def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False
    ceiling = int(math.ceil(math.sqrt(num)) + 1)
    for factor in xrange(3, ceiling, 2):
        if num % factor == 0:
            return False

    return True


def rotate(num):
    return int(str(num)[1:] + str(num)[0])


def rotations(num):
    answer = []
    cur_num = str(num)
    while cur_num not in answer:
        answer.append(cur_num)
        cur_num = cur_num[1:] + cur_num[0]

    return [int(a) for a in answer]


if __name__ == '__main__':
    circular_primes = 0
    primes = []

    for x in xrange(1000000):
        if all(is_prime(r) for r in rotations(x)):
            circular_primes += 1
            primes.append(x)

    print circular_primes
    print primes
