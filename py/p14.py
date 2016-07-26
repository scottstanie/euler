cache = {}


def collatz(n):
    length = 1
    current = n
    while current != 1:
        # if current in cache:
            # cache[n] = length + cache[current]
            # return cache[current]
        if current % 2 == 0:
            current /= 2
        else:
            current = (3 * current) + 1
        length += 1

    # cache[n] = length
    return length

if __name__ == '__main__':
    print collatz(13)
    lengths = []
    max_length = 0
    max_num = 0
    for i in range(1, int(1e6)):
        # if i % 1000 == 0:
            # print cache
            # print 'Count: ', i
        new_length = collatz(i)
        if new_length > max_length:
            max_length = new_length
            max_num = i

            lengths.append((i, new_length))

    print i, max_length
    print sorted(lengths, key=lambda x: x[1], reverse=True)
