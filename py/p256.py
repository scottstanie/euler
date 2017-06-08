#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
2N binary digits can be placed in a circle so that all the N-digit clockwise subsequences are distinct.

For N=3, two such circular arrangements are possible, ignoring rotations:

    [0, 0, 0, 1, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1, 0, 1]

For the first arrangement, the 3-digit subsequences, in clockwise order, are:
000, 001, 010, 101, 011, 111, 110 and 100.

Each circular arrangement can be encoded as a number by concatenating the binary digits starting with the subsequence of all zeros as the most significant bits and proceeding clockwise. The two arrangements for N=3 are thus represented as 23 and 29:

00010111 2 = 23
00011101 2 = 29
Calling S(N) the sum of the unique numeric representations, we can see that S(3) = 23 + 29 = 52.

Find S(5).
"""
import sys
import itertools
from collections import deque


def make_subsequences(N):
    """Returns a generator of all binary subsequences of length N"""
    return itertools.product((0, 1), repeat=N)


def make_circles(N):
    circle_len = 2**N
    return (circle for circle in itertools.product((0, 1), repeat=circle_len))


def check_circle(circle, N, all_subsequences):
    """Validates if a binary circle has all distinct subsequences

    Args:
        circle (list): a binary subsequence ring
        N (int): the subsequence length to check for
        all_subsequences (set): the set of all length N binary subsequences
    """

    c_len = len(circle)
    # The circle will have even 1s and 4 0s
    if sum(circle) != (c_len / 2):
        return False

    subsequences = set()
    circle_deq = deque(circle)
    for i in range(c_len):
        subsequences.add(tuple(itertools.islice(circle_deq, 0, N)))
        circle_deq.rotate()

    return subsequences == all_subsequences


def main():
    N = int(sys.argv[1])
    all_subsequences = set(make_subsequences(N))
    total_sum = 0
    for circle in make_circles(N):
        if sum(circle[:N]) > 0:
            break
        if check_circle(circle, N, all_subsequences):
            total_sum += int(''.join(str(c) for c in circle), 2)  # Int takes a base to convert

    print("Total sum: ", total_sum)

if __name__ == '__main__':
    main()
