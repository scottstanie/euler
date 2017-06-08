from p4 import is_pal


def rev_sum(n):
    return int(str(n)) + int(str(n)[::-1])


count = 0
for test in range(10000):
    iters = 0
    while iters < 50:
        iters += 1
        lych = True
        test = rev_sum(test)
        if is_pal(test):
            lych = False
            break

    if lych:
        count += 1

print count
