import math
for i in range(3, 2000000):
    if sum(math.factorial(int(d)) for d in str(i)) == i:
        print i
