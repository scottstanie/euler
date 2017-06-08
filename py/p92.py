def next_chain(n):
    return sum(int(d)**2 for d in str(n))

counter = {89: 0, 1: 0}

for n in range(1, int(10e6)):
    cur = n
    while cur not in (1, 89):
        cur = next_chain(cur)

    counter[cur] += 1

print counter
