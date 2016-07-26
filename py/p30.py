def fifth_sum(n):
    return sum(int(i)**5 for i in str(n))

total = 0
for i in range(2, 1000000):
    if i == fifth_sum(i):
        total += 1

print total
