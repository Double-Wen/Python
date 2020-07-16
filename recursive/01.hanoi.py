#!/usr/bin/env python3


def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        print("%s -> %s" % (a, c))
        hanoi(n-1, b, a, c)


if __name__ == '__main__':
    hanoi(20, 'A', 'B', 'C')
