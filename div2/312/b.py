#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter


def solve(n, xs):
    rxs = list(reversed(xs))
    length = len(xs)
    counter = Counter(xs)
    m = counter.most_common(1)[0][1]
    maxs = map(lambda x: x[0], filter(lambda x: x[1] == m, counter.most_common()))
    r = float('inf')
    rf = 0
    rl = 0
    for x in maxs:
        first = xs.index(x)
        last = length - rxs.index(x) - 1
        l = last - first + 1
        if r > l:
            r = l
            rf = first
            rl = last
    return rf + 1, rl + 1


def getinput():
    def getints_line():
        return list(map(int, input().split(' ')))
    n = int(input())
    xs = getints_line()
    return n, xs


def test():
    # print(solve(5, [1, 1, 2, 2, 1]))
    # print(solve(5, [1, 2, 2, 3, 1]))
    # print(solve(6, [1, 2, 2, 1, 1, 2]))
    assert solve(5, [1, 1, 2, 2, 1]) == (1, 5)
    assert solve(5, [1, 2, 2, 3, 1]) == (2, 3)
    assert solve(6, [1, 2, 2, 1, 1, 2]) == (1, 5)


def main():
    # test()
    # print(*getinput())
    print(' '.join(map(str, solve(*getinput()))))
    # print('\n'.join(map(str, solve(*getinput()))))

if __name__ == '__main__':
    main()
