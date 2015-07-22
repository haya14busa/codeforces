#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fact(n - 1)


def nCr(n, r):
    return fact(n) // (fact(r) * fact(n - r))


def modc(a, b, m=(10 ** 9 + 7)):
    c = 1
    for i in range(b):
        c = c * (a - i) % m
        c = c * modinv(i + 1, m) % m
    return c


def egcd(a, b):
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return (lastx, lasty, a)


def modinv(a, m):
    (inv, q, gcd_val) = egcd(a, m)
    return inv % m


def solve(h: int, w: int, bs):
    '''
    blackmap: {(int, int): 0}
    '''
    mod = (10 ** 9 + 7)
    dp = [[None for _ in range(w)] for _ in range(h)]
    dp[0][0] = 1
    bs = sorted(map(lambda t: (t[0] - 1, t[1] - 1), bs))
    bs.append((h - 1, w - 1))
    for i, (r, c) in enumerate(bs):
        s = 0
        for j in range(i):
            bj = bs[j]
            s += (dp[bj[0]][bj[1]] * modc(r + c - bj[0] - bj[1], c - bj[1]) + mod) % mod
        # dp[r][c] = (modc(r + c, r) - s) % (10 ** 9 + 7)
        dp[r][c] = ((modc(r + c, r) - s) + mod) % mod
    return dp[h - 1][w - 1]


def getinput():
    def getints_line():
        return list(map(int, input().split(' ')))
    h, w, n = getints_line()
    return h, w, [tuple(getints_line()) for _ in range(n)]


def test():
    art = Assert()
    art.equal(solve(3, 4, [(2, 2), (2, 3)]), 2)
    art.equal(solve(100, 100, [(15, 16), (16, 15), (99, 88)]), 545732279)


def main():
    test()
    # print(solve(*getinput()))
    # print('\n'.join(map(str, solve(*getinput()))))


class Assert(unittest.TestCase):
    def equal(self, a, b):
        self.assertEqual(a, b)

if __name__ == '__main__':
    main()
