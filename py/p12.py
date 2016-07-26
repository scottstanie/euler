# def factors(n):
#     factors = [i for i in range(2, int(math.ceil(math.sqrt(n)))) if n % i == 0]
#     return factors + [1, n]


def factors(n):
    '''The faster way'''
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def triangle_numbers():
    i = 1
    current_sum = 1
    while True:
        yield current_sum
        i += 1
        current_sum += i


if __name__ == '__main__':
    triangle_gen = triangle_numbers()
    t = triangle_gen.next()
    count = 1
    while len(factors(t)) <= 500:
        if count % 1000 == 0:
            f = factors(t)
            print t, len(f), f
        t = triangle_gen.next()
        count += 1

    print t
