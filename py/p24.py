from itertools import permutations

# "Permutations are emitted in lexicographic sort order."
count = 0
p = permutations('0123456789')
while count < 1e6:
    perm = p.next()
    count += 1

print ''.join(perm)
