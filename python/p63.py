# How many n-digit positive integers exist which are also an nth power?

def power_length(base, exp):
    return len(str(base**exp))


def is_powerful(base, exp):
    return power_length(base, exp) == exp


def find_power_numbers(exp):
    '''For a given exponent/ number length,
    find how many numbers satisfy'''
    count = 0
    base = 1
    while power_length(base, exp) <= exp:
        if is_powerful(base, exp):
            count += 1

        base += 1
    return count

if __name__ == '__main__':
    count = 0
    exp = 0

    still_more = True
    while still_more:
        # Find all numbers that match for new exponent
        exp += 1
        new_count = find_power_numbers(exp)
        count += new_count

        if new_count == 0:
            still_more = False

    print count
