from fractions import Fraction


def form_frac(iters):
    '''too much depth :('''
    if iters < 1:
        return 2
    else:
        return 2 + Fraction(1, form_frac(iters - 1))


def form_frac_iter(iters):
    # Yield as you go, don't recalculate
    f = 2
    yield Fraction(1) + Fraction(1, f)
    for i in range(iters):
        f = 2 + Fraction(1, f)
        yield Fraction(1) + Fraction(1, f)

count = 0
for f in form_frac_iter(1000):
    if len(str(f.numerator)) > len(str(f.denominator)):
        count += 1

print count
