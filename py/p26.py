def find_repeat_length(n):
    divs = 0
    divided = []
    d = 1
    while d > 0 and d not in divided:
        while d % n == d:
            d *= 10

        # print d, divided
        if d in divided:
            break
        divided.append(d)
        d = d % n
        divs += 1
        # print d
        # print divided

    return len(divided)


print find_repeat_length(19)
print find_repeat_length(29)
max_len = 0
max_d = 0
for i in range(3, 10000):
    length = find_repeat_length(i)
    if length > max_len:
        max_len = length
        max_d = i

print max_len, max_d
