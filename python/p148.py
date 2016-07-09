from scipy.misc import comb


def pascal_row(n):
    '''Return row n of pascal's triange, except for end 1s'''
    return (int(comb(n, i + 1)) for i in range(n - 1))


def is_div_7(n):
    return n % 7 == 0


if __name__ == '__main__':
    count = 0
    for idx in range(7, 1000001):
        try:
            count += sum(is_div_7(i) for i in pascal_row(idx))
        except:
            print idx

    print count
