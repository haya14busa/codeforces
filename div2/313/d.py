#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


def solve(a, b):
    ''' O(nlog(n)) '''
    def msort(s):
        l = len(s)
        if l % 2:
            return s
        mid_idx = l // 2
        s1 = msort(s[:mid_idx])
        s2 = msort(s[mid_idx:])
        return s1 + s2 if s1 < s2 else s2 + s1
    return msort(a) == msort(b)


def getinput():
    def getints_line():
        return list(map(int, input().split(' ')))
    return input(), input()


def test():
    art = Assert()
    art.equal(solve('aaba', 'abaa'), True)
    art.equal(solve('aabb', 'abab'), False)


def main():
    # test()
    print('YES' if solve(*getinput()) else 'NO')
    # print('\n'.join(map(str, solve(*getinput()))))


class Assert(unittest.TestCase):
    def equal(self, a, b):
        self.assertEqual(a, b)

if __name__ == '__main__':
    main()

