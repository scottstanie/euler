def sort_value(name_list, name):
    return name_list.index(name) + 1


def name_value(name):
    start = ord('A') - 1
    return sum((ord(s) - start for s in name))

if __name__ == '__main__':
    with open('p22_names.txt', 'r') as f:
        names = f.readline().replace('"', '').split(',')

    names.sort()

    print 'Names: ', names[:5]
    scores = 0
    for idx, name in enumerate(names):
        scores += ((1 + idx) * name_value(name))
        if name == 'COLIN':
            print 'COLIN score check: ', ((1 + idx) * name_value(name))

    print 'Total: ', scores
