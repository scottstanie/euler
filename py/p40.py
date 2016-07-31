from operator import mul

champ = ''.join(str(i) for i in range(200000))  # length will be > 1e6

digits = [10**p for p in range(7)]

print reduce(mul, (int(champ[d]) for d in digits))
