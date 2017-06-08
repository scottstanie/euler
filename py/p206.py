import math
# Slow :(
s = '1_2_3_4_5_6_7_8_9_0'
start = int(math.sqrt(1020304050607080900))

while str(start**2)[::2] != s[::2]:
    start += 1

print start
