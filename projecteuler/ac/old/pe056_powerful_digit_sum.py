#!/usr/bin/env python
# coding=utf-8
"""
Powerful digit sum
Problem 56


A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the
maximum digital sum?
"""
from __future__ import print_function
from pe016_power_digit_sum import sum_digit

if __name__ == '__main__':
    val = 0
    for a in range(1, 100):
        for b in range(1, 100):
            val = max(val, sum_digit(a ** b))
    print(val)  # 972
