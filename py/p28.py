import sys


def count_diags(square_size):
    diag = 1
    cur_increment = 2  # Current square size
    num_incs = 4  # 4 sides of the square
    yield diag  # yield 1 first
    while diag < square_size**2:
        diag += cur_increment
        num_incs -= 1
        if num_incs < 1:
            num_incs = 4
            cur_increment += 2

        yield diag

if __name__ == '__main__':
    print sum(count_diags(int(sys.argv[1])))
