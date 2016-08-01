def pandigitals(d):
    cur_prod = ''
    digits = set()
    for n in range(1, 6):
        cur = str(d * n)
        dset = set(cur)
        # print '*', cur_prod
        # print '---', digits
        if digits.intersection(dset):
            if digits == set('123456789'):
                return cur_prod
            break
        else:
            digits = digits.union(cur)

        cur_prod += cur
        if digits == set('123456789'):
            return cur_prod


pandigitals(192)
max_ = 0
for d in range(1, 10000):
    max_ = max(max_, pandigitals(d))

print max_
