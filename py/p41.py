from p35 import is_prime

max_prime = 0
for i in range(13, 10000000, 2):
    if not is_prime(i):
        continue
    n = len(str(i))
    digits = set(''.join(str(d) for d in range(1, n + 1)))
    if set(str(i)) == digits:
        max_prime = i

print max_prime
