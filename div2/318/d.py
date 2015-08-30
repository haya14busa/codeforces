#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AUTHOR: haya14busa
import sys
import io

def is_ok(hs):
    for h in hs:
        if h > 0:
            return False
    return True

# def solve(n, hs):
#     # n: n towers
#     assert 1 <= n <= 10 ** 5
#     # for h in hs:
#     #     assert 1 <= h <= 10 ** 9
#     cnt = 0
#     while not is_ok(hs):
#         cnt += 1
#         ph = 0  # prev height
#         nhs = []  # next height of towers
#         for h in hs:
#             if ph < h:
#                 nhs.append(ph)
#             else:
#                 if nhs:
#                     nhs[-1] = min([nhs[-1], h])
#                 nhs.append(h - 1)
#             ph = h
#         nhs[-1] = 0
#         hs = nhs
#     return cnt


def solve(n, hs):
    # n: n towers
    assert 1 <= n <= 10 ** 5
    for h in hs:
        assert 1 <= h <= 10 ** 9
    mh = max(hs)



def getinput():
    def getint():
        return int(input())

    def getints_line():
        return list(map(int, input().split(' ')))

    def getints(n):
        return [getint() for _ in range(n)]

    def getints_lines(n):
        return [getints_line() for _ in range(n)]
    return [getint(), getints_line()]


def iosolve():
    return str(solve(*getinput()))
    # return 'YES' if solve(*getinput()) else 'NO' # for boolean output
    # return '\n'.join(map(str, solve(*getinput()))) # for multiple line output


def main():
    if sys.stdin.isatty():
        test()
    stdin_lines = getstdin_lines()
    sys.stdin = io.StringIO('\n'.join(stdin_lines))
    if stdin_lines:
        print(iosolve())
    else:
        test()


def test():
    IO_TEST_CASES = [

        (
            # INPUT
            '''\
6
2 1 4 6 2 2
            ''',
            # EXPECT
            '''\
3
            '''
        ),

        (
            # INPUT
            '''\
7
3 3 3 1 3 3 3
            ''',
            # EXPECT
            '''\
2
            '''
        ),

        (
            # INPUT
            '''\
1
1
            ''',
            # EXPECT
            '''\
1
            '''
        ),

        (
            # INPUT
            '''\
2
1 5
            ''',
            # EXPECT
            '''\
1
            '''
        ),



    ]

    # List[(List[arg for solve()], expect)]
    TEST_CASES = [
        # ([], None),
    ]

    # You do need to see below
    import unittest  # to save memory, import only if test required
    import sys
    import io

    class Assert(unittest.TestCase):
        def equal(self, a, b):
            self.assertEqual(a, b)

        def float_equal(self, actual, expect, tolerance):
            self.assertTrue(expect - tolerance < actual < expect + tolerance)

    art = Assert()

    for inputs, expect in TEST_CASES:
        art.equal(solve(*inputs), expect)

    for stdin, expect in IO_TEST_CASES:
        sys.stdin = io.StringIO(stdin.strip())
        art.equal(iosolve(), expect.strip())
        # art.float_equal(float(iosolve()), float(expect.strip()), 10 ** -6)


def getstdin_lines():
    stdin = []
    while 1:
        try:
            stdin.append(input())
        except EOFError:
            break
    return stdin

if __name__ == '__main__':
    main()
