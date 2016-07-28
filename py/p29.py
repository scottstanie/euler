from itertools import product

a = b = range(2, 101)
print len({p[0] ** p[1] for p in product(a, b)})

# Alternate:
# print len({a**b for a in range(2, 101) for b in range(2, 101)})
