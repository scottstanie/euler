from p22 import name_value

triangle_values = {i * (i + 1) / 2 for i in range(100)}

with open('p042_words.txt') as f:
    words = f.read().replace('"', '').split(',')
    print sum(1 for word in words if name_value(word) in triangle_values)
