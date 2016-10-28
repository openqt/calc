# coding=utf-8
"""
Diophantine equation
Problem 66

Consider quadratic Diophantine equations of the form:

    x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is
square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:

    3^2 – 2×2^2 = 1
    2^2 – 3×1^2 = 1
    9^2 – 5×4^2 = 1
    5^2 – 6×2^2 = 1
    8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is
obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value
of x is obtained.
"""
from __future__ import print_function
from e0046_goldbachs_other_conjecture import is_square_number
from e0064_odd_period_square_roots import sqrt_cf


# def continued_fraction(a, b):
#     """to continued fraction expression
#
#     :param a:
#     :param b:
#     :return:
#     """
#     while b > 0:
#         r, a = divmod(a, b)
#         yield int(r)
#         a, b = b, int(a)


def converget_cf(cf, count=-1):
    """get value from continued fraction

    :param cf: continued fraction expression
    :param count:
    :return:
    """
    if len(cf) < 2:
        return

    p, q = [1, cf[0]], [0, 1]
    while True:
        for i in cf[1:]:
            if count == 0:
                return
            count -= 1

            yield p[1], q[1]
            p[0], p[1] = p[1], i * p[1] + p[0]
            q[0], q[1] = q[1], i * q[1] + q[0]


def pell(D):
    for x, y in converget_cf(sqrt_cf(D)):
        if x * x - D * y * y == 1:
            return x, D


if __name__ == '__main__':
    print(max(pell(D) for D in range(2, 1001) if not is_square_number(D))) # 661