class Node(object):
    def __init__(self, data, row_num, col_num):
        self.data = data
        self.position = (row_num, col_num)
        self.adjacent = []

    def __repr__(self):
        return 'Node: %s: %s' % (self.data, self.position)


def next_possible(row_idx, col_idx):
    '''The reachable indices from a column index'''
    return row_idx + 1, [col_idx, col_idx + 1]


numbers =       [  [75],
                 [95, 64],
               [17, 47, 82],
              [18, 35, 87, 10],
             [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34],
          [88, 2, 77, 73, 7, 63, 67],
         [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
       [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
     [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
   [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
 [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

END_NODE = Node(0, 15, 0)
position_to_nodes = {}
node_list = []
for row_idx, row in enumerate(numbers):
    for col_idx, num in enumerate(row):
        n = Node(num, row_idx, col_idx)
        position_to_nodes[(row_idx, col_idx)] = n
        node_list.append(n)

for position, node in position_to_nodes.iteritems():
    next_row, next_cols = next_possible(*node.position)
    if next_row > 14:
        node.adjacent.append(END_NODE)
    else:
        for col in next_cols:
            node.adjacent.append(position_to_nodes[(next_row, col)])


MAX_SUM = 0


def bfs(start, end):
    global MAX_SUM
    queue = []
    # One path to begin: path with only the starting node
    queue.append([start])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            current_sum = sum(p.data for p in path)
            if current_sum > MAX_SUM:
                MAX_SUM = current_sum
        else:
            for adj in node.adjacent:
                # Make a copy to add all adjacent nodes
                new_path = list(path)
                new_path.append(adj)
                queue.append(new_path)

path = bfs(node_list[0], END_NODE)
print path
# print sum(p.data for p in path)
print MAX_SUM
