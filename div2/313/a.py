#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


def solve(n, xs):
    return -1 if 1 in xs else 1


def getinput():
    def getints_line():
        return list(map(int, input().split(' ')))
    n = int(input())
    return n, getints_line()


def test():
    art = Assert()
    # x = 1
    art.equal(solve(5, [1, 2, 3, 4, 5]), -1)
    art.equal(solve(2, [2, 3]), 1)
    art.equal(solve(3, [1, 3, 4]), -1)
    # pass


def main():
    # test()
    print(solve(*getinput()))
    # print('\n'.join(map(str, solve(*getinput()))))


class Assert(unittest.TestCase):
    def equal(self, a, b):
        self.assertEqual(a, b)

if __name__ == '__main__':
    main()
