def prev_edges(row_idx, col_idx):
    '''The reachable indices from the last row
    max and min in placw to prevent out of bounds errors'''
    return row_idx - 1, [max(0, col_idx - 1), min(col_idx, row_idx - 1)]


# numbers =       [  [75],
#                  [95, 64],
#                [17, 47, 82],
#               [18, 35, 87, 10],
#                   ....

with open('p067_triangle.txt', 'r') as f:
    lines = f.readlines()
    numbers = [l.strip('\n').split(' ') for l in lines]
    numbers = [[int(n) for n in row] for row in numbers]
    print numbers[:5]
    for row_idx, row in enumerate(numbers):
        if row_idx == 0:
            # Skip the first row, no previous paths
            continue
        for col_idx, number in enumerate(row):
            prev_row_idx, (col1, col2) = prev_edges(row_idx, col_idx)
            # At each new row, check the previous two ways you could have reached this number
            # The max path to this point will just be the larger of the two paths plus the number
            numbers[row_idx][col_idx] += max(numbers[prev_row_idx][col1], numbers[prev_row_idx][col2])


print numbers[-1]
print max(numbers[-1])
