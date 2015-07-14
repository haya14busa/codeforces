#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(n, xs):
    '''
    最初公倍数を求める
    '''
    fs = [0 for _ in xs]

    def go(flag = True):
        m = min(xs)
        for i, x in enumerate(xs):
            cnt = 0
            while x > m:
                cnt += 1
                x = x // 2
            fs[i] += cnt
            xs[i] = x
            if x < m:
                m = x
                flag = False
                go(flag)
                break
        return flag
    flag = go()
    if flag:
        fs = sorted(fs)
        s = fs[len(fs) // 2]
        return sum([abs(s - f) for f in fs])
    else:
        return sum(fs)


def getinput():
    def getints_line():
        return list(map(int, input().split(' ')))
    n = int(input())
    return n, getints_line()


def test():
    assert solve(3, [4, 8, 2]) == 2
    assert solve(3, [3, 5, 6]) == 5
    assert solve(4, [4, 8, 2, 9]) == 3
    assert solve(4, [4, 5, 9, 16]) == 7
    pass


def main():
    # test()
    print(solve(*getinput()))
    # print('\n'.join(map(str, solve(*getinput()))))

if __name__ == '__main__':
    main()
