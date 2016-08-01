import itertools


def split_prod(str_n, idx):
    return str_n[:idx], str_n[idx:]


def find_mults(left):
    for idx in range(len(left) - 1):
        yield left[:idx + 1], left[idx + 1:]


solutions = []
for digits in itertools.permutations('123456789'):
    digits = ''.join(digits)
    split_idx = 5
    left, right = split_prod(digits, split_idx)
    for mult1, mult2 in find_mults(left):
        if int(mult1) * int(mult2) == int(right):
            solutions.append((mult1, mult2, right))

solution_prods = [int(s[2]) for s in solutions]
print solution_prods
print 'Deduped: ', set(solution_prods)
print sum(set(solution_prods))
