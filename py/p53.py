from scipy.misc import comb


count = 0
for n in range(1, 101):
    for r in range(1, n):
        if comb(n, r) > 1e6:
            count += 1

print count
