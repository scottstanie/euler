from fractions import Fraction


def cancel(num, den):
    old_frac = Fraction(num, den)
    nums = set(str(num))
    dens = set(str(den))
    common_digit = nums.intersection(dens)
    if not common_digit or common_digit == {'0'}:
        # print 1
        return False
    try:
        # cn = int(''.join(n for n in str(num) if n not in common_digit))
        cn = nums - common_digit
        if len(cn) != 1:
            # print 2
            return False
    except:
        print n, d
        return False
    try:
        # dn = int(''.join(n for n in str(den) if n not in common_digit))
        dn = dens - common_digit
        if len(dn) != 1:
            # print 3
            return False
    except:
        print n, d
        return False
    # print cn, dn
    (cn, ) = cn
    (dn, ) = dn
    if cn == dn or dn == '0':
        # print 4
        return False

    try:
        new_frac = Fraction(int(cn), int(dn))
    except:
        print cn, dn
        raise
    return new_frac == old_frac

print cancel(49, 98)
print '----'
total = Fraction(1, 1)
for n in range(10, 100):
    for d in range(n + 1, 100):
        if n == d:
            continue
        if cancel(n, d):
            print '%s / %s' % (n, d)
            total *= Fraction(n, d)

print total
