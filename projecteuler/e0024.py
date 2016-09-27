# coding=utf-8
"""
Lexicographic permutations
Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
from __future__ import print_function


def next_permutation(seq):
    """next permutation by lexicographic order

    :param seq: sequence
    :return: next permutation
    """
    i = len(seq) - 2
    while i >= 0 and seq[i] >= seq[i + 1]:  # look for down seq
        i -= 1

    if i >= 0:
        j = -1
        while seq[j] < seq[i]:
            j -= 1
        seq[i], seq[j] = seq[j], seq[i]  # switch ...

    i += 1
    j = len(seq) - 1
    while i < j:
        seq[i], seq[j] = seq[j], seq[i]
        i += 1
        j -= 1

    return seq


if __name__ == '__main__':
    seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = 1
    while n < 1000000:
        n += 1
        next_permutation(seq)
    print(seq)  # 2783915460
