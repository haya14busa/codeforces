#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Lala Land has exactly n apple trees
Tree number i is located in a position xi and has ai apples growing on it

Obj: wants to collect apples from the apple trees
Start: Amr currently stands in x = 0 position
'''


def solve(n, xas):
    minus = sorted([xa for xa in xas if xa[0] < 0])
    minus_len = len(minus)
    plus = sorted([xa for xa in xas if xa[0] > 0])
    plus_len = len(plus)
    d = abs(minus_len - plus_len)
    if d < 2:
        pass
    elif minus_len < plus_len:
        plus = plus[:-(d - 1)]
    else:
        minus = minus[d - 1:]
    return sum(map(lambda x: x[1], minus)) + sum(map(lambda x: x[1], plus))


def getinput():
    def getints_line():
        return list(map(int, input().split(' ')))
    n = int(input())
    xas = [getints_line() for _ in range(n)]
    return n, xas


def test():
    # print(solve(2, [[-1, 5], [1, 5]]))
    # print(solve(3, [[-2, 2], [1, 4], [-1, 3]]))
    # print(solve(3, [[1, 9], [3, 5], [7, 10]]))
    assert solve(2, [[-1, 5], [1, 5]]) == 10
    assert solve(3, [[-2, 2], [1, 4], [-1, 3]]) == 9
    assert solve(3, [[1, 9], [3, 5], [7, 10]]) == 9


def main():
    # test()
    print(solve(*getinput()))
    # print('\n'.join(map(str, solve(*getinput()))))

if __name__ == '__main__':
    main()
