from fractions import Fraction

fracs = list(set(Fraction(n, d) for d in range(1, 10000) for n in range(1, d)))
print 'Fractions listed'
print len(fracs)
fracs.sort()
print 'Fractions sorted'
search_idx = fracs.index(Fraction(3, 7))
print fracs[search_idx - 1]
