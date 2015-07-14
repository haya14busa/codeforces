#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(n, xs):
    counter = {}
    for i, x in enumerate(xs):
        if x in counter:
            counter[x]['cnt'] += 1
            counter[x]['last'] = i
        else:
            counter[x] = {'cnt': 0, 'first': i, 'last': i}
    ts = sorted(counter.items(), key=lambda t: t[1]['cnt'], reverse=True)
    mv = 0  # max value
    mr = float('inf')  # max range
    rkey = 0  # result key
    for t in ts:
        k, d = t
        r = d['last'] - d['first']
        if mv <= d['cnt'] and mr > r:
            mv = d['cnt']
            mr = r
            rkey = k
    return counter[rkey]['first'] + 1, counter[rkey]['last'] + 1


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
