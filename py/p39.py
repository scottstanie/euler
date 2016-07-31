import itertools
from collections import Counter
import math


def combos(n):
    '''Finds all integer triplet combinations up to n'''
    for a, b in itertools.combinations_with_replacement(xrange(1, n + 1), 2):
        yield (a**2, b**2, a**2 + b**2)


perim_counter = Counter()


def count_combos(a2, b2, c2):
    a = math.sqrt(a2)
    b = math.sqrt(b2)
    c = math.sqrt(c2)
    p = a + b + c
    # If the perimeter of the triplet is under 1000, count this triplet
    if p <= 1000:
        perim_counter[p] += 1

for a2, b2, c2 in combos(1000):
    count_combos(a2, b2, c2)

# Show the top 3 perimeters with the most triplet possibilities
print perim_counter.most_common(3)
