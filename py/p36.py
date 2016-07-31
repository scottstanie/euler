from p4 import is_pal

print sum(n for n in range(1000000) if is_pal(n) and is_pal("{:b}".format(n)))
