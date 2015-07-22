#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(a, b, c, d, e, f) -> bool:
    def tri(n):
        return n + n * (n - 1)
    l = a + b + c
    return tri(l) - (tri(a) + tri(c) + tri(e))


def getinput():
    def getints_line():
        return list(map(int, input().split(' ')))
    return getints_line()


def test():
    art = Assert()
    art.equal(solve(1, 1, 1, 1, 1, 1), 6)
    art.equal(solve(1, 2, 1, 2, 1, 2), 13)
    art.equal(solve(2, 1, 2, 1, 2, 1), 13)
    art.equal(solve(2, 2, 2, 2, 2, 2), 24)
    art.equal(solve(2, 3, 2, 3, 2, 3), 37)
    art.equal(solve(3, 3, 3, 3, 3, 3), 54)


def main():
    # test()
    print(solve(*getinput()))
    # print('\n'.join(map(str, solve(*getinput()))))


import unittest
class Assert(unittest.TestCase):
    def equal(self, a, b):
        self.assertEqual(a, b)

if __name__ == '__main__':
    main()

