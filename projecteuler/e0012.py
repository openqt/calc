"""
Highly divisible triangular number
Problem 12

The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""
from __future__ import print_function
from e0003 import prime_sieve


def len_factors_brute_force(n):
    """number of factors of number
     For every exact divisor up to the square root,
     there is a corresponding divisor above the square root.
    https://en.wikipedia.org/wiki/Integer_factorization

    :param n: number
    :return: factor sequence
    """
    if n < 3:
        return n

    count = 1
    i = 2
    while i < n ** .5:
        if n % i == 0:
            count += 1
        i += 1
    count *= 2
    if i ** 2 == n:
        count += 1
    return count


def prime_factors(n):
    """generate prime factors of number

    :param n: number
    :return: prime factors sequence
    """
    if n < 2:
        return

    for i in prime_sieve(int(n ** .5)):
        if i * i > n:
            break

        while n % i == 0:
            yield i
            n /= i

    if n > 1:
        yield n


def len_factors_by_prime(n):
    caches = {}
    for i in prime_factors(n):
        caches[i] = caches.setdefault(i, 0) + 1

    count = 1
    for v in caches.values():
        count *= v + 1
    return count


def triangle_number(stop=None):
    """generate triangle sequence

    :param stop: the maximum number
    :return: triangle sequence
    """
    number = 1
    step = 1
    while True:
        yield number

        step += 1
        number += step
        if stop and number > stop:
            break


if __name__ == '__main__':
    for i in triangle_number():
        length = len_factors_by_prime(i)
        if length > 500:
            print(i, length)  # 76576500 576
            break
