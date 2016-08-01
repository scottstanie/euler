from p35 import is_prime


def find_goldbach():
    # Meh, reasonable test sizes for primes/ squares
    two_squares = [2 * (i**2) for i in range(10000)]
    primes = {i for i in range(100000) if is_prime(i)}
    test = 3
    while True:
        if is_prime(test):
            test += 2
            continue
        for s in two_squares:
            if test - s in primes:
                test += 2
                break
        else:
            return test

if __name__ == '))main__':
    print find_goldbach()
