from num2words import num2words

total = 0
for i in range(1, 1001):
    # print num2words(i)
    total += len(num2words(i).replace('-', '').replace(' ', ''))

print total
